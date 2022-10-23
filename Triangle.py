#  File: Triangle.py

#  Description: This program the maximum path from 
#               several methods (brute force, greedy, divide and conquer,
#               and dynamic progress), by only moving to adjacent numbers.

#  Student Name: Michael Pham

#  Student UT EID: mp46987

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 3/2/2022

#  Date Last Modified: 3/3/2022

import sys

from timeit import timeit

# returns the greatest path sum using exhaustive search
def brute_force (grid):
    index1 = 0
    index2 = 0
    journey = []
    total_sum = 0
    brute_force_helper(grid, index1, index2, journey, total_sum)
    #Below return the maximum of the journey
    return max(journey)

    
def brute_force_helper(grid, index1, index2, journey, total_sum):
    if index1 >= len(grid):
    #This is if the code reaches the bottom of the triangle
        journey.append(total_sum)
        return
    #Returns bottom of triangle
    else:
        total_sum += grid[index1][index2]
    #The below code will return either the bottom left or bottom right value
    return brute_force_helper(grid, index1 + 1, index2 + 1, journey, total_sum) or brute_force_helper(grid, index1 + 1, index2, journey, total_sum)
        
    
    

# returns the greatest path sum using greedy approach
def greedy (grid):
    index = 0
    greatest_sum = 0
    for x in range(len(grid)):
        greatest = 0
        temp = 0
        if len(grid[x]) < 3:
            greatest = grid[x][0].max(grid[x][1])
            #Adding to the high sum in a direction
            greatest_sum += greatest
        else:
            for y in range(index, index + 2):
                if greatest < grid[x][y]:
                    greatest = grid[x][y]
                    temp = y
            #The paths sum is being added onto here
            greatest_sum += greatest
            index = temp
    return greatest_sum
    #return greatest journey


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
    #This returns the value from the helper
    return divide_conquer_helper(grid, len(grid), 1, grid[0][0], 0)


def divide_conquer_helper(grid, a, current_sum, all_sums, b):
    if current_sum == a:
        #Returns if already at the end 
        return all_sums
    
    x = divide_conquer_helper(grid, a, current_sum + 1, all_sums + grid[current_sum][b], b)
    y = divide_conquer_helper(grid, a, current_sum + 1, all_sums + grid[current_sum][b + 1], b + 1)
    
    #Find the max direction we can go in and return that value to divide_conquer
    return max(x,y)
    
# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
    #loops through 2d array starting from the bottom point
    for x in range(len(grid) - 2, -1, -1):
        for y in range(x + 1):
            #comparing the two numbers and adding it on
            if (grid[x + 1][y] > grid[x + 1][y + 1]):
                grid[x][y] += grid[x + 1][y]
            else:
                grid[x][y] += grid [x + 1][y + 1]
    return grid[0][0]

# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  '''
  # check that the grid was read in properly
  print (grid)
  '''

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print('The geratest path sum through exhaustive search is')
  print(brute_force(grid))
  print('The time taken for exhaustive approach in seconds is')
  print(times)

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print('The geratest path sum through greedy search is')
  print(brute_force(grid))
  print('The time taken for greedy approach in seconds is')
  print(times)

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print('The geratest path sum through recursive search is')
  print(brute_force(grid))
  print('The time taken for recursive approach in seconds is')
  print(times)

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print('The geratest path sum through dynamic programming is')
  print(brute_force(grid))
  print('The time taken for dynamic programming in seconds is')
  print(times)
  
  
if __name__ == "__main__":
  main()
