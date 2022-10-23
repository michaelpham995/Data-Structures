#  File: Boxes.py

#  Description: This program utilizies memoization and other
#               techniques to find largest subset of boxes that could be nested inside 
#               of each other. I had a tough time figuring out the memoization 
#               based of the current format so I looked at the Spring 2021 assignment outline
#               for motivation to solve. 

#  Student Name: Michael Pham

#  Student UT EID: mp46987

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 3/8/2022

#  Date Last Modified: 3/10/2022

import sys

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes

def nesting_boxes (all_sets): #Change input name to fit with program 
    nested_list = []
    for x in all_sets:
        #If no subsets
        if len(x) == 0:
            continue
        
        #Establishing beginning and index ranges for recursive purpsoses
        list_of_sets = [x[0],]
        end = 1
        begin = 0
        memo_nesting(begin, end, nested_list, list_of_sets, x)
        
    maximum = 0 
    for a in nested_list:
        if len(a) > maximum:
            maximum = len(a)
    #Above finds the most boxes that can fit inside one another
    
    counter = 0
    for a in nested_list:
        if len(a) == maximum:
            counter += 1
    #Above finds the most amount of times maximum can be achieved
                
    return maximum, counter #Returns our two output values


        

#Below is a memo created where we return lists to run the recursionof nesting boxes
def memo_nesting(begin, end, nested_list, list_of_sets, x):
    
    if end >= len(x): #best case
        if list_of_sets in nested_list:
            return
        else:
            nested_list.append(list_of_sets)
            return
        
    if does_fit(x[begin], x[end]):
        list_of_sets.append(x[end])
        begin = end #Equilizes
        memo_nesting(begin, end + 1, nested_list, list_of_sets, x)
    else:
        memo_nesting(begin, end + 1, nested_list, list_of_sets, x)

            

def box_sets(box_list, list_fits, point, all_sets):
    if point == len(box_list):
        all_sets.append(list_fits)
        return #Best case
    else:
        #add to subset on first recursion and incrememt indexes on both of them 
        alternative_set = list_fits[:] #This creates the opposing sets
        list_fits.append(box_list[point])
        box_sets(box_list, list_fits, point + 1, all_sets)
        box_sets(box_list, alternative_set, point + 1, all_sets)
        

    
    
# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)
    

  list_fits = []
  all_sets = []
  # print to make sure that the input was read in correctly
  #print (box_list)
  #print()

  # sort the box list
  box_list.sort()

  # print the box_list to see if it has been sorted.
  #print (box_list)
  #print()
  
  #This is additional function to help 
  box_sets(box_list, list_fits, 0, all_sets)
  # get the maximum number of nesting boxes and the
  # number of sets that have that maximum number of boxes
  max_boxes, num_sets = nesting_boxes (all_sets)

  # print the largest number of boxes that fit
  print (max_boxes)

  # print the number of sets of such boxes
  print (num_sets)

if __name__ == "__main__":
  main()
