#  File: TestBinaryTree.py

#  Description: In this assignment we add to the Node and Tree classes and add the methods
#               get_level, get_height, is_similar, and num_nodes. We then test these methods on
#               our binary tree to see certain properties of the trees and specified nodes.

#  Student Name: Michael Pham

#  Student UT EID: mp46987

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 4/11/22

#  Date Last Modified: 4/12/22


import sys

class Node (object):
  def __init__(self, data):
      self.data = data
      self.leftC = None
      self.rightC = None
      #Above we establish the left and right childs for the tree

#Creates a string representation for later
  def __str__(self):
      string = ''
      return string


class Tree (object):
  def __init__(self):
      self.root = None
      #Needed to add data to make trees 

#
  def insert(self, data):
      node = Node(data)
      #Creating an instance
      if not self.root:
          self.root = node
      else:
          curr = self.root
          parent = self.root
          while curr:
              #If data is less then current then we put in left tree
              parent = curr
              if data < curr.data:
                  curr = curr.leftC
              else:
              #If data is greater than current we put in right tree
                  curr = curr.rightC
          if data < parent.data:
              #If data is less than we make node on left
              parent.leftC = node
          else:
              #on right if larger
              parent.rightC = node

  # Returns true if two binary trees are similar
  def is_similar (self, pNode): 
      return self.is_similar_helper(self.root, pNode, pNode.root)

  def is_similar_helper(self, first, p, second):
      if first:
          #If there the lengths of the trees are unequal or if second node does not exists
          if not second or first.data != second.data:
              return False
          #Recursively iterates through the tree to see if the trees are similar
          return self.is_similar_helper(first.leftC, p, second.leftC) and self.is_similar_helper(first.rightC, p, second.rightC)
      return second == None

  # Returns a list of nodes at a given level from left to right
  def get_level (self, level): 
      val_level = []
      #Calls the helper function to find the level of the tree
      self.get_level_helper(level, 0, self.root, val_level)
      return val_level

  def get_level_helper(self, level, beg, first, val_level):
      if first:
          #If we are on the specified level then we can add
            if beg == level:
                val_level.append(first)
            else:
                #If this is not the end of the binary tree we will iterate down
                self.get_level_helper(level, beg + 1, first.leftC, val_level)
                self.get_level_helper(level, beg + 1, first.rightC, val_level)
                #Will give us the value of the level that will be returned to get level function

  # Returns the height of the tree
  def get_height (self): 
      return self.get_height_helper(self.root, -1)
  
  def get_height_helper(self, first, height):
      #For the function we are just adding 1 for everytime to node comes back as existing
      #Then we return max of left and right sides because one can always be larger than the other
      if first:
          return max(self.get_height_helper(first.leftC, height + 1), self.get_height_helper(first.rightC, height + 1))
      return height


  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree and the root
  def num_nodes (self):
      #Returns from the helper function the number of nodes that we have
    return self.num_nodes_helper(self.root)
  
  def num_nodes_helper(self, first):
      if first:
          #If there is an existing node then return up
          return 1 + self.num_nodes_helper(first.rightC) + self.num_nodes_helper(first.leftC)
      return 0 #This is if there is no trees or nodes existing

def main():
    # Create three trees - two are the same and the third is different
	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree1_input = list (map (int, line)) 	# converts elements into ints

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree2_input = list (map (int, line)) 	# converts elements into ints

	line = sys.stdin.readline()
	line = line.strip()
	line = line.split()
	tree3_input = list (map (int, line)) 	# converts elements into ints

    # Test your method is_similar()

    # Print the various levels of two of the trees that are different

    # Get the height of the two trees that are different

    # Get the total number of nodes a binary search tree

if __name__ == "__main__":
  main()