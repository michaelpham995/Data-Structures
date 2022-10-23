
# -*- coding: utf-8 -*-
#  File: Intervals.py

#  Description: This project collapses intervals and then organizes them
# based on the order. 

#  Student Name: Michael Pham

#  Student UT EID: mp46987

#  Partner Name: 

#  Partner UT EID: 

#  Course Name: CS 313E 

#  Unique Number: 51125

#  Date Created: January 29th

#  Date Last Modified: February 8th




'''
How to use this Template:
For this assignment, do not change the function names or parameters
You will need to read from standard input. In order to do this, when 
you run your program in the command line, you will do it as follows:

$ python3 Intervals.py < intervals.in

If you read intervals.in as a file, it will not work on HackerRank. 
You should be able to paste this whole file into HackerRank. Please 
run your code to ensure it passes, and write your own test cases to 
ensure your answer is correct.
'''


import sys

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval

def merge_tuples (tuples_list):
    
    tuples_list.sort()
    imported_list = []
    
    for a in range(len(tuples_list)):
        imported_list.append(list(tuples_list[a]))
        
    merged = []
    merged.append(imported_list[0])
    
    x = 0
    
    for y,z in imported_list[1:]:
        if merged[x][1] > z:
            del(imported_list[x + 1])
        elif merged[x][1] >= y:
            merged[x][1] = z
            del(imported_list[x + 1])
        else:
            x += 1
            merged.append(imported_list[x])
            
    merge_results = []
    
    for a in range(len(merged)):
        placeholder = tuple(merged[a])
        merge_results.append(placeholder)
        
    return merge_results


    
    

# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval




def sort_by_interval_size (tuples_list):
    
    sorting_list = [tuple(x) for x in tuples_list]
    sorted_list = sorted(sorting_list, key = lambda y: abs(y[0]-y[1]))
    
    return sorted_list




# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
     assert merge_tuples([(1,2)]) == [(1,2)] #This is very convenient to use!
      # write your own test cases
    
     assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
      # write your own test cases
    
     return "all test cases passed"

def main():
  # open file intervals.in and read the data and create a list of tuples

  # merge the list of tuples

  # sort the list of tuples according to the size of the interval

  # run your test cases
  '''
  print (test_cases())
  '''

  # write the output list of tuples from the two functions

    # merge the list of tuples

    
  # sort the list of tuples according to the size of the interval

  # write the output list of tuples from the two functions
    
  all_tuples = []
  x = int(sys.stdin.readline())
  
  for a in range(x):
     line = sys.stdin.readline()
     x, y = (int(z) for z in line.split())
     imported_formatted = (x, y)
     all_tuples.append(imported_formatted)
     
  merged = merge_tuples(all_tuples)
  print(merged)

  ordered = sort_by_interval_size(merged)
  print(ordered)

if __name__ == "__main__":
  main()