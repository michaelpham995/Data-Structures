#  File: Poly.py

#  Description: This program takes in different polynomials 
# and outputs the sum and product in descending order of the exponenets. 

#  Student Name: Michael Pham

#  Student UT EID: mp46987

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 4/3/2022

#  Date Last Modified: 4/6/2022

import sys

class Link (object):
  def __init__ (self, coeff = 1, exp = 1, next = None):
    self.coeff = coeff
    self.exp = exp
    self.next = next

  def __str__ (self):
    return '(' + str (self.coeff) + ', ' + str (self.exp) + ')'

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # keep Links in descending order of exponents
  def insert_in_order (self, coeff, exp):
      current = self.first
      before = self.first
      addlink = Link(coeff, exp)

      if not current:
          #If there is nothing in the LinkedList, then add a value as the first
          addlink.next = current
          self.first = addlink
          return
        
      while current.exp >= exp:
          before = current
          current = current.next
          if not current:
              #If the current exponent is the smallest one, place it at the end of the list
              before.next = addlink
              return
      if current == self.first:
          #Add to the front
          addlink.next = current
          self.first = addlink
          return

      before.next = addlink
      addlink.next = current
      #Here we add the seen link between the before and current link 


  # add polynomial p to this polynomial and return the sum
  def add (self, p):
      currentadd = self.first
      pcurrent = p.first
      addpolynomial = LinkedList()

      if not currentadd:
          return p
      if not p.first:
          return self
      #If either of the given lists are empty we return the one with information in it 

      #If both of the lists still has information, we will add them 
      while pcurrent and currentadd:
          if currentadd.exp == pcurrent.exp:
              #Add equivalent exponenets
              newcoefficient = currentadd.coeff + pcurrent.coeff
              if newcoefficient > 0:
                  addpolynomial.insert_in_order(newcoefficient, currentadd.exp)
              currentadd = currentadd.next
              pcurrent = pcurrent.next
          elif currentadd.exp > pcurrent.exp:
              #If the self list is larger exponentially, we add it 
              addpolynomial.insert_in_order(currentadd.coeff, currentadd.exp)
              currentadd = currentadd.next
          else:
              addpolynomial.insert_in_order(pcurrent.coeff, pcurrent.exp)
              pcurrent = pcurrent.next

      #Remaining values from the self list, if the p list runs out
      while currentadd:
          #Here we are combining like terms
          add = currentadd.coeff
          while currentadd.next and currentadd.exp == currentadd.next.exp:
              add += currentadd.next.coeff
              currentadd = currentadd.next
          addpolynomial.insert_in_order(add, currentadd.exp)
          currentadd = currentadd.next

      #Remaining values foom p list
      while pcurrent:
          #Combining like terms
          add = pcurrent.coeff
          while pcurrent.next and pcurrent.exp == pcurrent.next.exp:
              add += pcurrent.next.coeff
              pcurrent = pcurrent.next
          addpolynomial.insert_in_order(add, pcurrent.exp)
          pcurrent = pcurrent.next
      return addpolynomial


  def combine_like_terms(self):
      if self.first:
          current = self.first
          while current:
              nextterm = current.next
              while nextterm and nextterm.exp == current.exp:
                  #This tests to see if the exponent value matches one another
                  current.coeff += nextterm.coeff
                  #Adds the coefficients of the exponents into one
                  current.next = nextterm.next
                  nextterm = nextterm.next
              current = current.next
      return
              #iterating on to the next value
    
    

  # multiply polynomial p to this polynomial and return the product
  def mult (self, p):
      if not self.first:
          return p
      elif not p.first:
          return self
      else:
        multpolylist = LinkedList()
        #Above creates the list we return and a dummy list to return values
        currentself = self.first
        while currentself:
            currentp = p.first
            while currentp:
                #For each self list we iterate through each p list and multiply it by that
                multpolylist.insert_in_order(currentself.coeff * currentp.coeff, currentself.exp + currentp.exp)
                #Store added elements in the dummy list to be added later
                currentp = currentp.next
            currentself = currentself.next
        return multpolylist



  # create a string representation of the polynomial
  def __str__ (self):
      current = self.first
      finalpoly = ""
      #Base case, if there is nothing there. 
      if not current:
          return finalpoly
      while current.next:
          if current.coeff != 0:
            finalpoly += '(' + str (current.coeff) + ', ' + str (current.exp) + ')' + ' + '
          current = current.next
      #This is because we do not need a '+' after final term
      finalpoly += '(' + str (current.coeff) + ', ' + str (current.exp) + ')'
      return finalpoly

def main():
  # read data from file poly.in from stdin
  # create polynomial p
  line = sys.stdin.readline()
  polynomialp = LinkedList()
  for i in range(int(line)):
      line = sys.stdin.readline().split()
      polynomialp.insert_in_order(int(line[0]), int(line[1]))

  line = sys.stdin.readline()
  line = sys.stdin.readline()

  # create polynomial q
  polynomialq = LinkedList()
  for i in range(int(line)):
      line = sys.stdin.readline().split()
      polynomialq.insert_in_order(int(line[0]), int(line[1]))


  # get sum of p and q and print sum
  polynomialsum = polynomialp.add(polynomialq)
  polynomialsum.combine_like_terms()
  print(polynomialsum)

  # get product of p and q and print product
  polynomialproduct = polynomialp.mult(polynomialq)
  polynomialproduct.combine_like_terms()
  print(polynomialproduct)

if __name__ == "__main__":
  main()
