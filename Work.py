#  File: Work.py 

#  Description: This calculates the minimum number of lines via linear and 
#binary search that must be written before the first cup of coffee. 

#  Student Name: Michael Pham

#  Student UT EID: mp46987

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 2/20/2022

#  Date Last Modified: 2/21/2022

import sys, time


def num_lines_series(a: int, k: int) -> int:
    
    y = 1
    x = a
    
    while (a // k ** y) > 0:
        x += a // k ** y
        y += 1
        
    return x
    
# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee

  
def linear_search(n: int, k: int) -> int:
  # use linear search here

    for x in range(1, n + 1):
        #Utilizes the num series function added to make this work
        if num_lines_series(x, k) >= n:
            return x
     
  
# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
  # use binary search here
    
    maximum = n
    minimum = 0
    mean = (maximum +  minimum) // 2
    
    #This is caluclating the min and max productivity factors with the code
    while maximum != mean and mean != minimum:
        if num_lines_series(mean, k) < n:
            minimum = mean
            mean = (maximum + minimum) // 2
        elif num_lines_series(mean, k) > n:
            maximum = mean
            mean = (maximum + minimum) // 2
        else:
            return mean
    return mean + 1
    


# main has been completed for you
# do NOT change anything below this line
def main():
  num_cases = int((sys.stdin.readline()).strip())

  for i in range(num_cases):
    inp = (sys.stdin.readline()).split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()