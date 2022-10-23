#  File: Hull.py

#  Description: This program takes in a set of points and finds the smallest
# convex polygon that will exclose these points. It then calculates the area
# and outputs it to the system.


#  Student Name: Michael Pham

#  Student UT EID: mp46987

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 2/14/2022

#  Date Last Modified: 2/16/2022

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  return (p.x * q.y) + (q.x * r.y) + (p.y * r.x) - (r.y * p.x) - (r.x * q.y) - (p.y * q.x)

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):
    
    #Establishing lists for the hulls bounds
    max_hull = []
    max_hull.append(sorted_points[0])
    max_hull.append(sorted_points[1])

    imported_length = len(sorted_points)
    
    for x in range(2, imported_length):
        #we are appending imports to the max length, skip the first 2 bc they cant be max
        max_hull.append(sorted_points[x])
        while len(max_hull) >= 3 and det(max_hull[-3], max_hull[-2], max_hull[-1]) >= 0:
            #If hulls are greater than 0, and there are enough points we delete the -2 element
            del max_hull[-2]
    
    min_hull = []
    min_hull.append(sorted_points[0])
    min_hull.append(sorted_points[1])    
    
    reverse_hull = sorted_points[::-1]
    for x in range(2, len(reverse_hull)):
        #add length in different order
        min_hull.append(reverse_hull[x])
        while len(min_hull) >= 3 and det(min_hull[-3], min_hull[-2], min_hull[-1]) >= 0:
                del min_hull[-2]
        
        
    max_hull.pop(0)
    min_hull.pop(-1)
    
    #Appending all the coords to the max hull
    
    total_hull = max_hull + min_hull
    
    return total_hull
                
    

# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
    
    print('')
    determinant1 = 0
    determinant2 = 0
    
    for x in range(len(convex_poly)):
        if x == len(convex_poly) - 1:  #The endpoint
        #adding the determinants together
            determinant2 = (convex_poly[x].x * convex_poly[0].y)
            determinant2 = determinant1 + determinant2
            determinant1 = determinant2           
        else:
            determinant2 = (convex_poly[x].x * convex_poly[x + 1].y)
            determinant2 = determinant1 + determinant2
            determinant1 = determinant2
            
    for x in range(len(convex_poly)):
        if x == (len(convex_poly) - 1):
            determinant2 = (convex_poly[x].y * convex_poly[0].x)
            determinant2 = determinant1 - determinant2
        else:
            #matrix determinant
            determinant2 = (convex_poly[x].y * convex_poly[x + 1].x)
            determinant2 = determinant1 - determinant2
            determinant1 = determinant2
        
    #Calculate the areaof the polygon
    polygon_area = abs(determinant2) * 0.5
    return polygon_area
            


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases

  return "all test cases passed"

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
    sort = sorted(points_list)
    #Is this where i messed up?
  '''
  # print the sorted list of Point objects
  for p in sorted_points:
    print (str(p))
  '''

  # get the convex hull
  receive_hull = convex_hull(sort)

  # run your test cases

  # print your results to standard output
  
  # print the convex hull
  print('Convex Hull')
  for x in receive_hull:
      print(x)
      
  # get the area of the convex hull
  convex_hull_area = area_poly(receive_hull)
  
  # print the area of the convex hull
  print("Area of Convex Hull =", end = ' ')
  print(convex_hull_area)
  

if __name__ == "__main__":
  main()