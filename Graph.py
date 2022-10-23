#  File: Graph.py

#  Description: We are adding to the graph class by adding functions such as BFS to go through map and
#               delete functions that will allow us to remove parts of the graph. 

#  Student Name: Michael Pham

#  Student UT EID: mp46987

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 4/19/22

#  Date Last Modified: 4/20/22




import sys
from unicodedata import ucd_3_2_0

class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append (item)

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check the item on the top of the stack
  def peek (self):
    return self.stack[-1]

  # check if the stack if empty
  def is_empty (self):
    return (len (self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len (self.stack))


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue is empty
  def is_empty (self):
    return (len (self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len (self.queue))

  #This function will give us the first item in the queue
  def top(self):
      return self.queue[0]


class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False    #Flag that tells us if we visited vertex yet

  # determine if a vertex was visited
  def was_visited (self):
    return self.visited

  # determine the label of the vertex
  def get_label (self):
    return self.label

  # string representation of the vertex
  def __str__ (self):
    return str (self.label)

#We are going to use adjency matrix to represent graph
#An edge class is something that may be on the third exam

class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.adjMat = []
    #Constraint - every label is unique


  # check if a vertex is already in the graph
  def has_vertex (self, label):
    nVert = len (self.Vertices)
    #This is a sequential search that we are running
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return True
    return False

  # given the label get the index of a vertex
  def get_index (self, label):
    nVert = len (self.Vertices)
    #Sequential search
    for i in range (nVert):
      if (label == (self.Vertices[i]).get_label()):
        return i
    return -1

  # add a Vertex with a given label to the graph
  def add_vertex (self, label):
    # Checkst o see if the vertex already exists
    if (self.has_vertex (label)):
      return

    # add vertex to the list of vertices
    self.Vertices.append (Vertex (label))

    # add a new column in the adjacency matrix
    nVert = len (self.Vertices)
    for i in range (nVert - 1):
      (self.adjMat[i]).append (0)

    # add a new row for the new vertex
    new_row = []
    for i in range (nVert):
      new_row.append (0)
    self.adjMat.append (new_row)      

  # add weighted directed edge to graph
  def add_directed_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight

  # add weighted undirected edge to graph
  def add_undirected_edge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight

  # return an unvisited vertex adjacent to vertex v (index)
  def get_adj_unvisited_vertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()): #Greater than 0 means there is an edge for column 
        return i
    return -1

  # This function returns weight between two given vertices
  def get_weight(self, fromLabel, toLabel):
      begin = self.get_index(fromLabel)
      end = self.get_index(toLabel)
      if begin or end == -1:
          return -1
          #Return -1 if non-existent
      if self.adjMat[begin][end] == 0:
          return -1
          #Return -1 if non-existent
      else:
          return self.adjMat[begin][end]
          #Returning the weight 

  def vertices(self):
      return self.Vertices
      #We are returning vertexes for later use

  #If there are no neigbors the list will be empty, returns list of immediate neighbors
  def neighbors(self, neighborLabel):
      nVert = len(self.Vertices)
      adjacent_neighbors = []
      begin = self.get_index(neighborLabel)
      #Above we set our starting vertex to test from 
      for x in range(nVert):
          if self.adjMat[begin][x] != 0:
              #This tests to see if there is a neighbor there
              adjacent_neighbors.append(x)
      return adjacent_neighbors
      #We are returning the list of adjacent neighbors here


  # do a depth first search in a graph
  def dfs (self, v):
    # create the Stack
    theStack = Stack ()

    # mark the vertex v as visited and push it on the Stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    # visit all the other vertices according to depth
    while (not theStack.is_empty()):
      # get an adjacent unvisited vertex
      u = self.get_adj_unvisited_vertex (theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push (u)

    # the stack is empty, let us rest the flags
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False

  # do the breadth first search in a graph
  def bfs (self, v):
    theQueue = Queue()
    searched = set() #Creates set to hold discovered values

    self.Vertices[v].visited = True
    #Below will print out the first value
    #Accidently forgot on previous submission that I dequeued it before printing
    print(self.Vertices[v])
    #We mark as visited and then add to the enqueue
    theQueue.enqueue(v)
    #Also we add it to the searched set
    searched.add(v)

    while not theQueue.is_empty():
        #Visit until our queue is done for
        u = self.get_adj_unvisited_vertex(theQueue.top())
        if u == -1:
            u = theQueue.dequeue()
        else:
            if u not in searched:
                #If we have not found u yet, we add it to queue and mark as visited
                theQueue.enqueue(u)
                print(self.Vertices[u])
                self.Vertices[u].visited = True

  #This will delete a vertex
  def remove_vert(self, label):
      if self.has_vertex(label):
          delval = self.get_index(label)
          self.adjMat.pop(delval) #Here we are deleting the row of the vertex (Reverse of earlier)
          #Now we have to move onto column
      for i in range(len(self.adjMat)):
          self.adjMat[i].pop(delval)
          #Here the column is officially being popped (each row loses 1 value)
      self.Vertices.pop(delval)
      #Above we are officially deleting vertex from list of verticies

  #This removes single or double edges depending on if graph is directed
  def remove_edge(self, beginLabel, endLabel):
      #Set the inputs
      begin = self.get_index(beginLabel)
      end = self.get_index(endLabel)
      self.adjMat[begin][end] = 0
      self.adjMat[end][begin] = 0


def main():
  # create the Graph object
  cities = Graph()

  # read the number of vertices
  line = sys.stdin.readline()
  line = line.strip()
  num_vertices = int (line)

  # read the vertices to the list of Vertices
  for i in range (num_vertices):
    line = sys.stdin.readline()
    city = line.strip()
    cities.add_vertex (city)

  # read the number of edges
  line = sys.stdin.readline()
  line = line.strip()
  num_edges = int (line)

  # read each edge and place it in the adjacency matrix
  for i in range (num_edges):
    line = sys.stdin.readline()
    edge = line.strip()
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])

    cities.add_directed_edge (start, finish, weight)

  # read the starting vertex for dfs and bfs
  line = sys.stdin.readline()
  start_vertex = line.strip()

  # get the index of the starting vertex
  start_index = cities.get_index (start_vertex)

  # do the depth first search
  print ("Depth First Search")
  cities.dfs (start_index)
  print ()

  #This is breadth first search
  print("Breadth First Search")
  cities.bfs(start_index)
  print()

  #This reads in the deletion input
  line = sys.stdin.readline()
  delete_edge = line.strip()
  delete_edge = line.split()
  start = (delete_edge[0])
  end = (delete_edge[1])
  print("Deletion of an edge")
  cities.remove_edge(start, end)

  #The new adjacency matrix
  print()
  print("Adjacency Matrix")
  for x in range(num_vertices):
      for y in range(num_vertices):
          if y == num_vertices - 1:
              print(cities.adjMat[x][y])
              #If last in row
          else:
              print(cities.adjMat[x][y], end = " ")
              #Added space
  print()

  #This reads in vertex deletion
  line = sys.stdin.readline()
  vertexToRemove = line.strip()
  print('Deletion of a vertex')
  cities.remove_vert(vertexToRemove)
  print()

  #This is the list of verticies
  print('List of Vertices')
  for x in cities.Vertices:
      print(x)

  #The next adjacency Matrix
  num_vertices = len(cities.Vertices)
  print()
  print('Adjacency Matrix')
  for x in range(num_vertices):
      for y in range(num_vertices):
          if y == num_vertices - 1:
              #If last in row
              print(cities.adjMat[x][y])
          else:
              print(cities.adjMat[x][y], end = ' ')
    
if __name__ == "__main__":
  main()
