
#  File: Geometry.py

#  Description: This tests a series of different shapes and points
# and tells whether certain inputs, are inside, outside, intersect
# these shapes and objects. 

#  Student Name: Michael Pham

#  Student UT EID: mp46987

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: February 3

#  Date Last Modified: Febrary 5

import math
import sys


def distance_between_points(p, q):
    
    center = Point(0,0,0)
    message = ''
    if p.distance(center) > q.distance(center):
        message = 'is'
    else:
        message = 'is not'
    return 'Distance of Point p from the origin ' + message + ' greater than the distance of Point q from the origin'
    
      

      
def max_and_min(verticies, a_cube):
    
    corners = []
    points = [[.5, -.5, -.5], [.5, .5, -.5], [.5, .5, .5],
            [.5, -.5, .5], [-.5, -.5, -.5], [-.5, .5, -.5],
            [-.5, .5, .5], [-.5, -.5, .5]]
    for point in points:
        corners.append(Point(a_cube.center.x + (point[0] * a_cube.side), a_cube.center.y + (point[1] * a_cube.side), a_cube.center.z + (point[2] * a_cube.side)))
    
    
    maximum = [corners[0].x, corners[0].y, corners[0].y]
    minimum= [corners[0].x, corners[0].z, corners[0].z]
    
    for point in corners:
        if point.x > maximum[0]:
            maximum[0] = point.x
        elif point < maximum[0]:
            maximum[0] = point.x
        if point.y > maximum[1]:
            maximum[1] = point.y
        elif point.y < maximum[1]:
            maximum[1] = point.y
        if point.z > maximum[2]:
            maximum[2] = point.z
        elif point.z < maximum[2]:
            maximum[2] = point.z
            
    return maximum, minimum


class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
      
      self.x = x
      self.y = y
      self.z = z
      
  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
      
      return '({}, {}, {})'.format(float(self.x), float(self.y), float(self.z))

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
      
     return math.sqrt((float(self.x) - float(other.x)) ** 2.0 + (float(self.y) - float(other.y)) ** 2.0 + (float(self.z) - float(other.z)) ** 2.0)

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
      
      total = 1.0e-8
      return (abs(self.x - other.x) < total) and (abs(self.y - other.y) < total) and (abs(self.z - other.z) < total)
  
  def x_y_dist(self, other):
      
      return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
      
      self.r = float(radius)
      self.center = Point(x, y, z)
      self.x = x
      self.y = y
      self.z = z

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
      
      return 'Center: ({}, {}, {}), Radius: {}'.format(float(self.x), float(self.y), float(self.z), float(self.r))

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
      
      return math.pi * 4 * self.r ** 2

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
      
      return math.pi * (4/3) * self.r ** 3

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
      
      return Point.distance(p, self.center) < self.r

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
      
      centers = self.center.distance(other.center)
      return centers + other.r < self.r

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      
      x = float(a_cube.center.x)
      y = float(a_cube.center.y)
      z = float(a_cube.center.z)
      half = float(a_cube.side / 2)
      
      b1 = self.center.distance(Point((x + half), (y + half), (z + half / 2)))
      b2 = self.center.distance(Point((x - half), (y + half), (z + half / 2)))
      b3 = self.center.distance(Point((x + half), (y - half), (z + half / 2)))
      b4 = self.center.distance(Point((x - half), (y - half), (z + half / 2)))  
      t1 = self.center.distance(Point((x + half), (y + half), (z + half / 2)))
      t2 = self.center.distance(Point((x - half), (y + half), (z + half / 2)))
      t3 = self.center.distance(Point((x + half), (y - half), (z + half / 2)))
      t4 = self.center.distance(Point((x - half), (y - half), (z + half / 2)))
      
      if t1 > self.r or t2 > self.r or t3 > self.r or t4 > self.r:
          
          return False
      
      if b1 > self.r or b2 > self.r or b3 > self.r or b4 > self.r:
          
          return False
      
      return True

  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl):
      
      x = a_cyl.center.x
      y = a_cyl.center.y
      z = a_cyl.center.z
      half = a_cyl.r 
      
      b1 = Point((x + half), (y + half), (z - half / 2))
      b2 = Point((x - half), (y + half), (z - half / 2))
      b3 = Point((x + half), (y - half), (z - half / 2))
      b4 = Point((x - half), (y - half), (z - half / 2))
      t1 = Point((x + half), (y + half), (z + half / 2))
      t2 = Point((x - half), (y + half), (z + half / 2))
      t3 = Point((x + half), (y - half), (z + half / 2))
      t4 = Point((x - half), (y - half), (z + half / 2))
      
      if (self.is_inside_point(t1) == False) or (self.is_inside_point(t2) == False) or (self.is_inside_point(t3) == False) or (self.is_inside_point(t4) == False):
          return False
      
      if (self.is_inside_point(b1) == False) or (self.is_inside_point(b2) == False) or (self.is_inside_point(b3) == False) or (self.is_inside_point(b4) == False):
          return False
      
      return True
  
      for x in range(2):
          if x == 0:
              s_edge = self.center.x
              o_edge = a_cyl.center.x
          else:
              s_edge = self.center.y
              o_edge = a_cyl.center.y
              
          if (s_edge - self.r < o_edge - a_cyl.r < s_edge + self.r) is False:
              if (s_edge - self.r < o_edge + a_cyl.r < s_edge + self.r) is False:
                  return False
              
              
      if (self.center.z - self.r < a_cyl.center.z - a_cyl.h / 2 < self.center.z + self.r) is False:
          if (self.center.z - self.r < a_cyl.center.z + a_cyl.h / 2 < self.center.z + self.r) is False:
              return False
      else:
          return False

      return True


  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
      
      sphere_edge = self.r + other.r < self.center.distance(other.center)
      return not self.is_inside_sphere(other) and not sphere_edge


  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube):
      
      if self.is_inside_cube(a_cube):
          return False
      
      corner = math.hypot(math.hypot(a_cube.side / 2, a_cube.side / 2), a_cube.side / 2)
      return self.center.distance(a_cube.center) <= self.r + corner

  
  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
      
      side = math.hypot(self.r / 2, self.r / 2)
      
      return Cube(self.center.x, self.center.y, self.center.z, side)

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
      
      self.side = float(side)
      self.center = Point(x, y, z)
      self.x = x
      self.y = y
      self.z = z
  
  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
      
      return 'Center: ({}, {}, {}), Side: {}'.format(float(self.x), float(self.y), float(self.z), float(self.side))

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
      
      return (self.side ** 2) * 6

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
      
      return self.side ** 3

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
      
      outerbound = self.side / 2
      
      if (self.center.x - outerbound < p.x < self.center.x + outerbound) is False:
          return False
      
      if (self.center.y - outerbound < p.y < self.center.y + outerbound) is False:
          return False     
      
      if (self.center.z - outerbound < p.z < self.center.z + outerbound) is False:
          return False
      
      return True

      
  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      
      outerbound = self.side /2
      rad = a_sphere
      print(rad)
      for x in range(3):
          if x == 0:
              s_edge = self.center.x
              o_edge = a_sphere.center.x
          elif x == 1:
              s_edge = self.center.y
              o_edge = a_sphere.center.y
          else:
              s_edge = self.center.z
              o_edge = a_sphere.center.z
              
          if (s_edge - outerbound < o_edge - rad < s_edge + outerbound) is True:
              if (s_edge - outerbound < o_edge + rad < s_edge + outerbound) is False:
                  return False
          else:
              return False
          
      return True
      

      
  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
      
      outerbound = self.side / 2
      other_outerbound = other.side / 2
      
      for x in range(3):
          if x == 0:
              s_edge = self.center.x
              o_edge = other.center.x
          elif x == 1:
              s_edge = self.center.y
              o_edge = other.center.y
          else:
              s_edge = self.center.z
              o_edge = self.center.z
              
          if (s_edge - outerbound < o_edge - other_outerbound < s_edge + outerbound) is True:
              if (s_edge - outerbound < o_edge + other_outerbound < s_edge + outerbound) is False:
                  return False
          else:
              return False
          
      return True
      

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
      
      points = [[1, 0, .5], [0, 1, 0.5],
                [0, -1, 0.5], [-1, 0, 0.5]]
      c_points = []
      
      for point in points:
          x_point = a_cyl.center.x + (point[0] * a_cyl.r)
          y_point = a_cyl.center.y + (point[1] * a_cyl.r)
          z_point = a_cyl.center.z + (point[2] * a_cyl.h)
          c_points.append(Point(x_point, y_point, z_point))
          c_points.append(Point(x_point, y_point, z_point - a_cyl.h))

      for point in c_points:
          if not self.is_inside_point(point):
              return False
      return True
  
  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  
  def corners(self):
    
      x = self.center.x
      y = self.center.y
      z = self.center.z
      half = self.side / 2
      edges = []
      
      
      
      edges.append(Point((x + half), (y + half), (z + half)))
      edges.append(Point((x - half), (y + half), (z + half)))
      edges.append(Point((x + half), (y - half), (z + half)))
      edges.append(Point((x - half), (y - half), (z + half)))  
      edges.append(Point((x + half), (y + half), (z + half)))
      edges.append(Point((x - half), (y + half), (z + half)))
      edges.append(Point((x + half), (y - half), (z + half)))
      edges.append(Point((x - half), (y - half), (z + half)))
      
      return edges
  
  
  def does_intersect_cube (self, other):
      
      if self.is_inside_cube(other) == True or other.is_inside_cube(self) == True:
          return False
      
      other_c = other.corners()
      self_c = self.corners()
      
      for edge in other_c:
          if self.is_inside_point(edge) == True:
              return True
      for self_edge in self_c:
          if other.is_inside_point(self_edge) == True:
              return True
      return False
  

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
      
      if self.does_intersect_cube(other):
          corners = []
          points = [[.5, -.5, -.5], [.5, .5, -.5], [.5, .5, .5],
                    [.5, -.5, .5], [-.5, -.5, -.5], [-.5, .5, -.5],
                    [-.5, .5, .5], [-.5, -.5, .5]]
          A_point = points(self)
          B_point = points(other)
          A_max, A_min = max_and_min(A_point)
          B_max, B_min = max_and_min(B_point)
          intersecting_points = []
          side_length = self.side + other.side
          
          for x in range(3):
              if A_max[x] > B_max[x]:
                  higher = A_max[x]
                  lower = B_max[x]
              else:
                  higher = B_max[x]
                  lower = B_max[x]
                
              if A_max[x] > B_min[x]:
                  higher = A_min[x]
                  lower = B_min[x]
              else:
                  higher = B_min[x]
                  lower = B_min[x]
              side_diff = side_length - abs(higher - lower)
              intersecting_points.append(side_diff)

          two_dimen_area = intersecting_points[0] * intersecting_points[1]
          area = two_dimen_area * intersecting_points[2]
          return area
      else:
          return 0

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):

      r = self.r
      return Sphere(self.center.x, self.center.y, self.center.z, r)


class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
      
      self.center = Point(x, y, z)
      self.r = radius
      self.h = height
      self.x = x
      self.y = y
      self.z = z
      
  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
      
      return 'Center: ({}, {}, {}), Radius: {}, Height: {}'.format(float(self.x), float(self.y), float(self.z), float(self.r), float(self.h))
  
  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
      
      return (math.pi * self.r * self.h * 2) + 2 * math.pi * self.r ** 2

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
      
      return math.pi * self.h * self.r ** 2

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
      
      if (self.center.z - self.h / 2 < p.z < self.center.z + self.h / 2) is False:
          return False
      
      return self.r > math.hypot((p.x - self.center.x), (p.y - self.center.y))
        

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      
      height = self.h
      max_z = self.center.z + height
      min_z = self.center.z - height
      
      sphere_z_minimum = a_sphere.center.z - a_sphere.r
      sphere_z_maximum = a_sphere.center.z + a_sphere.r
      
      center_differences = self.center.x_y_dist(a_sphere.center)
      return (abs(center_differences) + a_sphere.r < self.r) and (min_z < sphere_z_minimum < max_z) and (min_z < sphere_z_maximum < max_z)
  

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):

      for x in range(2):
          if x == 0:
              s_edge = self.center.x
              o_edge = a_cube.center.x
          else:
              s_edge = self.center.y
              o_edge = a_cube.center.y
    
          if (s_edge - self.r < o_edge - a_cube.side < s_edge + self.r) is True:
              if (s_edge - self.r < o_edge + a_cube.side < s_edge + self.r) is False:
                  return False
          else:
              return False
          
          if (self.center.z - self.h / 2 < a_cube.center.z - a_cube.side / 2 < self.center.z + self.h / 2) is True:
              if (self.center.z - self.h / 2 < a_cube.center.z + a_cube.side / 2 < self.center.z + self.h / 2) is False:
                  return False
          else:
              return False
          
          return True      


  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
      
      for x in range(2):
          if x == 0:
              s_edge = self.center.x
              o_edge = other.center.x
          else:
              s_edge = self.center.y
              o_edge = other.center.y
    
          if (s_edge - self.r < o_edge - other.r < s_edge + self.r) is True:
              if (s_edge - self.r < o_edge + other.r < s_edge + self.r) is False:
                  return False
          else:
              return False
          
          if (self.center.z - self.h / 2 < other.center.z - other.h / 2 < self.center.z + self.h / 2) is True:
              if (self.center.z - self.h / 2 < other.center.z + other.h / 2 < self.center.z + self.h / 2) is False:
                  return False
          else:
              return False
          
          return True
      
  # determine if another Cylinder intersects this Cylinder
  # two Cylinder object intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other):
      
      if self.is_inside_cylinder(other) == True:
          return False
      if other.is_inside_cylinder(self) == True:
          return False
      
      if math.hypot((self.center.x - other.center.x), (self.center.y - other.center.y)) < (self.r + other.r):
          if ((self.center.z + self.h / 2) > (other.center.z - other.h/2)) == True:
              return True
          if ((self.center.z - self.h / 2) > (other.center.z + other.h/2)) == True:
              return True   
      else:
          return False
      
      return False
            
def main():
    
  a = Point(5,7)
  print(a)
  # read data from standard input
  p_sys = sys.stdin.readline().split()

  # read the coordinates of the first Point p
  for a in range(len(p_sys)):
      p_sys[a] = float(p_sys[a])

  # create a Point object 
  p = Point(p_sys[0], p_sys[1], p_sys[2])

  # read the coordinates of the second Point q
  q_sys = sys.stdin.readline().split()
  for a in range(len(q_sys)):
      q_sys[a] = float(q_sys[a])

  # create a Point object 
  q = Point(q_sys[0], q_sys[1], q_sys[2])
  
  # read the coordinates of the center and radius of sphereA
  firstsphere_in = sys.stdin.readline().split()
  for a in range(len(firstsphere_in)):
      firstsphere_in[a] = float(firstsphere_in[a])
      
  # create a Sphere object 
  firstsphere = Sphere(firstsphere_in[0], firstsphere_in[1], firstsphere_in[2] ,firstsphere_in[3])

  # read the coordinates of the center and radius of sphereB
  secondsphere_in = sys.stdin.readline().split()
  for a in range(len(secondsphere_in)):
      float(secondsphere_in[a]) - float(secondsphere_in[a])
  
  # create a Sphere object
  secondsphere = Sphere(secondsphere_in[0], secondsphere_in[1], secondsphere_in[2], secondsphere_in[3])


  # read the coordinates of the center and side of cubeA
  CubeA_in = sys.stdin.readline().split()
  for a in range(len(CubeA_in)):
      CubeA_in[a] = float(CubeA_in[a])

  # create a Cube object 
  CubeA = Cube(CubeA_in[0], CubeA_in[1], CubeA_in[2], CubeA_in[3])

  # read the coordinates of the center and side of cubeB
  CubeB_in = sys.stdin.readline().split()
  for b in range(len(CubeB_in)):
      CubeB_in[a] = float(CubeB_in[a])

  # create a Cube object
  CubeB = Cube(CubeB_in[0], CubeB_in[1], CubeB_in[2], CubeB_in[3])

  # read the coordinates of the center, radius and height of cylA
  cylA_in = sys.stdin.readline().split()
  for a in range(len(cylA_in)):
      cylA_in[a] = float(cylA_in[a])
      
  # create a Cylinder object 
  cylA = Cylinder(cylA_in[0], cylA_in[1], cylA_in[2], cylA_in[3], cylA_in[4])

  # read the coordinates of the center, radius and height of cylB
  cylB_in = sys.stdin.readline().split()
  for a in range(len(cylB_in)):
      cylB_in[a] = float(cylB_in[a])
      
  # create a Cylinder object
  cylB = Cylinder(cylB_in[0], cylB_in[1], cylB_in[2], cylB_in[3], cylB_in[4])

  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin
  print(distance_between_points(p, q))
  print()

  # print if Point p is inside sphereA
  if firstsphere.is_inside_point(p):
      print('Point p is inside sphereA')
  else:
      print('Point p is not inside sphereA')
         
  # print if sphereB is inside sphereA
  if secondsphere.is_inside_point(p):
      print('sphereB is inside sphereA')
  else:
      print('sphereB is not inside sphereA')

  # print if cubeA is inside sphereA
  if CubeA.is_inside_sphere(firstsphere):
      print('cubeA is inside sphereA')
  else:
      print('cubeA is not inside sphereA')

  # print if cylA is inside sphereA
  if cylA.is_inside_sphere(firstsphere):
      print('cubeA is inside sphereA')
  else:
      print('cubeA is not inside sphereA')

  # print if sphereA intersects with sphereB
  if firstsphere.does_intersect_sphere(secondsphere):
      print('sphereA does intersect sphereB')
  else:
      print('sphereA does not intersect sphereB')

  # print if cubeB intersects with sphereB
  if secondsphere.does_intersect_cube(CubeB):
      print('cubeB does intersect sphereB')
  else:
      print('cubeB does not intersect sphereB')
      
  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA
  if firstsphere.circumscribe_cube().volume() > cylA.volume():
      print('Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA')
  else:
      print('Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA')
  print()
  
  # print if Point p is inside cubeA
  if CubeA.is_inside_point(p):
      print('Point p is inside cubeA')
  else:
      print('Point p is not inside cubeA')

  # print if sphereA is inside cubeA
  if CubeA.is_inside_sphere(firstsphere):
      print('sphereA is inside cubeA')
  else:
      print('sphereA is not inside cubeA')
      
  # print if cubeB is inside cubeA
  if CubeA.is_inside_sphere(CubeB):
      print('sphereA is inside cubeA')
  else:
      print('sphereA is not inside cubeA')
      
  # print if cylA is inside cubeA
  if CubeA.is_inside_cylinder(cylA):
      print('cylA is inside cubeA')
  else:
      print('cylA is not inside cubeA')

  # print if cubeA intersects with cubeB
  if CubeA.does_intersect_cube(CubeB):
      print('cubeA does intersect cubeB')
  else:
      print('cubeA does not intersect cubeB')
      
  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA
  if CubeA.intersection_volume(CubeB) > firstsphere.volume():
      print('Intersection volume of cubeA and cubeB is greater than the volume of sphereA')
  else:
      print('Intersection volume of cubeA and cubeB is not greater than the volume of sphereA')  

  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA
  if CubeA.inscribe_sphere().area() > cylA.area():
      print('Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA')
  else:
      print('Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA')
  print()
    
  # print if Point p is inside cylA
  if cylA.is_inside_point(p):
      print('Point p is inside cylA')
  else:
      print('Point p is not inside cylA')

  # print if sphereA is inside cylA
  if cylA.is_inside_cube(CubeA):
      print('sphereA is inside cylA')
  else:
      print('sphereA is not inside cylA')

  # print if cubeA is inside cylA
  if cylA.is_inside_cube(CubeA):
      print('cubeA is inside cylA')
  else:
      print('cubeA is not inside cylA')
    
  # print if cylB is inside cylA
  if cylA.is_inside_cylinder(cylB):
      print('cylB is inside cylA')
  else:
      print('cylB is not inside cylA')
      
  # print if cylB intersects with cylA
  if cylA.does_intersect_cylinder(cylB):
      print('cylB does not intersect cylA')
  else:
      print('cyclB does not intersect cylA')

if __name__ == "__main__":
  main()