#  File: Radix.py

#  Description: This creates a radix sort that can sort different strings that have 
# combinations of letters (a-z) and numbers (0-9)

#  Student Name: Michael Pham

#  Student UT EID: mp46987

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 3/25/22

#  Date Last Modified: 3/26/22

import sys

class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))

# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
    
    #Below is a dictionary that gives the priority for each character in the radix sort
    radix_dictionary = {'0':0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6' : 6, '7':7, '8':8,
              '9':9, 'a':10, 'b':11, 'c':12, 'd':13, 'e':14,'f':15, 'g':16, 'h':17, 'i':18,
              'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25, 'q': 26, 'r' : 27,
              's': 28, 't': 29, 'u': 30, 'v': 31, 'w' :32, 'x':33, 'y':34, 'z' :35, '^': 0}
    
    indexes = []
    for x in range(36):
        indexes.append(Queue())
    #This creates an index for each of the characters in the dictionary
    
    longeststring = len(a[0])
    for x in range(1, len(a)):
        if len(a[x]) > longeststring:
            longeststring = len(a[x])
    #This finds the length of the longest string in the input
    
    
    #Makes each string the same length. 
    #Since ^ is given the value of 0 the shorter strings will still be ahead in the sort order
    for x in range(len(a)):
        while len(a[x]) < longeststring:
            a[x] = a[x] + '^'
    
    #This places each item into the an index based on character value in the dictionary
    for x in range(longeststring):
        for y in a:
            queued = radix_dictionary[y[len(y) - x - 1]]
            (indexes[queued]).enqueue(y)
    
        answer_order = []
        for x in range(36):
            while indexes[x].is_empty() == False:
                answer_order.append(indexes[x].dequeue())
                #Dequeues and adds to a different list
        a = answer_order
    
    
    #Reverts any changes we may have made
    answer = []
    for x in a:
        answer.append(x.replace('^', ''))
    
    
    return answer
    
    
        
def main():
  # read the number of words in file
  
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)
  
  
  # print word_list
  '''
  print (word_list)
  '''
  '''
  word_list = ['12', 'z34', '8fg6d', '42cb3f', 'sd67mn9', '7ty2d4', 'xc65ns3',
               '51s23', '720', 'knbw', 'plaq78d', '520ce8', 'ij9944']
  # use radix sort to sort the word_list
  '''
  sorted_list = radix_sort (word_list)
  
  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

    