#  File: OfficeSpace.py

#  Description: This program is designed to compute the number of 
#   square feet in an office space and prints out how it is used
#   based on the inputs that are placed. These include office space, 
#   unallocated space, contested space, and uncontested space that each employee gets.

#  Student Name: Michael Pham

#  Student UT EID: mp46987

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 2/7/22

#  Date Last Modified: 2/8/22

import sys

# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
    
    return (rect[2] - rect[0]) * (rect[3] - rect[1])

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
    
    overlapping_coords = (0, 0, 0, 0)
    
    if rect1[1] > rect2[3]:
        return overlapping_coords
    elif rect2[1] > rect1[3]:
        return overlapping_coords
    elif rect1[0] > rect2[2]:
        return overlapping_coords
    elif rect2[0] > rect1[2]:
        return overlapping_coords
    else:
        overlapping_coords = (max(rect1[0], rect2[0]), max(rect1[1], rect2[1]), min(rect1[2], rect2[2]), min(rect1[3], rect2[3]))
    return overlapping_coords


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
    
    area_of_unallocated_space = 0
    for a in range(len(bldg)):
        for b in range(len(bldg[a])):
            if bldg[a][b] == 0:
                area_of_unallocated_space += 1
    return area_of_unallocated_space


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
    
    area_contested_space = 0
    for a in range(len(bldg)):
        for b in range(len(bldg[a])):
            if bldg[a][b] > 1:
                area_contested_space += 1
    return area_contested_space


# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    
    area_uncontested_space = area(rect)
    for a in range(rect[0], rect[2]):
        for b in range(rect[1], rect[3]):
            if bldg[b][a] != 1:
                area_uncontested_space -= 1
    return area_uncontested_space


# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    
    employee_request = [[0 for a in range(office[2])] for b in range(office[3])]
    for space in cubicles:
        for a in range(space[0], space[2]):
            for b in range(space[1], space[3]):
                employee_request[b][a] += 1
    return employee_request
    
    
# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert area ((0, 0, 1, 1)) == 1
  # write your own test cases

  return "all test cases passed"

def main():
  # read the data
  
  employee_names = []
  cubicle_space = []
  
  office_inputs = sys.stdin.readline().strip()
  office_splits = office_inputs.split()
  office = (0,0, int(office_splits[0]), int(office_splits[1]))
  employee_count = int(sys.stdin.readline().strip())
  
  for a in range(employee_count):
      cell_request = sys.stdin.readline().strip()
      cr_split = cell_request.split()
      name = cr_split[0]
      area_of_request = (int(cr_split[1]), int(cr_split[2]), int(cr_split[3]), int(cr_split[4]))
      
      cubicle_space.append(area_of_request)
      employee_names.append(name)
      
  layout = request_space(office, cubicle_space)
      
      
  # run your test cases
  '''
  print (test_cases())
  '''

  # print the following results after computation

  # compute the total office space
  print('Total', area(office))

  # compute the total unallocated space
  print('Unallocated', unallocated_space(layout))
  

  # compute the total contested space
  print('Contested', contested_space(layout))

  # compute the uncontested space that each employee gets
  for a in range(len(employee_names)):
      print(employee_names[a], uncontested_space(layout, cubicle_space[a]))


if __name__ == "__main__":
  main()