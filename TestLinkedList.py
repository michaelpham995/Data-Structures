#  File: TestLinkedList.py

#  Description: This program utilizes helper mathods for LinkedList and tests 
#               by inserting integers.

#  Student Name: Michael Pham

#  Student UT EID: mp46987

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 3/30/22

#  Date Last Modified:

class Link (object):
    def __init__(self, data):
        self.next = None
        self.data = data
    
    def __str__(self):
        return str(self.data)

class LinkedList (object):
  # create a linked list
  # you may add other attributes
  def __init__ (self):
    self.first = None
    self.last = None
    self.length = 0
    #Establishing the first and last for our functions

  # get number of links 
  def get_num_links (self):
      return self.length
      #Return number of links
  
  # add an item at the beginning of the list
  def insert_first (self, data): 
      insert = Link(data)
      if self.length == 0:
          #If list empty add element at [0]
          self.first = insert
          self.last = insert
      else:
          #Insert element in front of [0] if filled
          insert.next = self.first
          self.first = insert
      self.length += 1
      
  # add an item at the end of a list
  def insert_last (self, data): 
      insert = Link(data)
      if self.length == 0:
          #If list empty add element at [0]
          self.first = insert
          self.last = insert
      else:
          #Insert element at end of list if not empty
          self.last.next = insert
          self.last = insert
      self.length += 1
      
          

  # add an item in an ordered list in ascending order
  # assume that the list is already sorted
  def insert_in_order (self, data): 
      insert = Link(data)
      if self.length == 0:
          self.first = insert
          self.last = insert
      #If the insert data is less than first move to front of list
      elif self.first.data >= insert.data:
          self.insert_first(insert.data)
      #Move to back of list if last < insert
      elif self.last.data <= insert.data:
          self.insert_last(insert.data)
      else:
          node = self.first
          #This will find where to insert inside linked list
          while node.data < insert.data:
              predecessor = node
              node = node.next
          insert.next = node
          predecessor.next = insert
      self.length += 1

  # search in an unordered list, return None if not found
  def find_unordered (self, data): 
      if self.length == 0:
          #If the list is empty we return None
          return None
      else:
          node = self.first
          while node:
              if node.data == data:
                  #This returns the node if it equals to data and we return it
                  return node
              node = node.next
      #If the data is not found return None
      return None
      

  # Search in an ordered list, return None if not found
  def find_ordered (self, data): 
      if self.length == 0:
          return None #Returns if the list is empty
      else:
          node = self.first
          while node:
              if node.data == data:
                  #If the node contains the data, return the node
                  return node
              node = node.next
              #Move on to the next node in the list
              #We do not need node.data < data
          return None    

  # Delete and return the first occurrence of a Link containing data
  # from an unordered list or None if not found
  def delete_link (self, data):
        previous = self.first
        current = self.first
        
        if (current == None):
            return None
        
        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next
                #Change pointer from previous data to next data that we want to delete
        
        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next
            
        return current
      

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
      if self.length == 0:
          return ""
          #If length is 0 there is no string
      else:
          string = ""
          string += str(self.first) + "  "
          char = 1
          #Adding initial string
          current = self.first.next
          while current:
              string += str(current) + "  "
              char += 1
              if char % 10 == 0:
                  #Ten items to a line, we skip if characters // 10 = 0
                  string += '\n'
              current = current.next
          return string
            
          
  # Copy the contents of a list and return new list
  # do not change the original list
  def copy_list (self):
      new_list = LinkedList()
      if self.length == 0:
          return new_list
          #Empty list if we are dealt an empty list
      current = self.first
      while current:
          new_list.insert_last(current.data)
          #Insert data at end so the list comes out the same
          current = current.next
      return new_list


  # Reverse the contents of a list and return new list
  # do not change the original list
  def reverse_list (self): 
      new_list = LinkedList()
      if self.length == 0:
          return new_list
          #If empty return empty
      current = self.first
      while current:
          new_list.insert_first(current.data)
          #Insert first so data is backwards
          current = current.next
      return new_list


  # Sort the contents of a list in ascending order and return new list
  # do not change the original list
  def sort_list (self): 
      new_list = LinkedList()
      if self.length == 0:
          return new_list
          #For empty list
      current = self.first
      while current:
          new_list.insert_in_order(current.data)
          current = current.next
      return new_list

  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
      if self.length <= 1:
          return True
          #Best case
      before = self.first
      current = self.first.next
      while current:
          if current.data <= before.data:
              #Checks to see if ascending
              return False
          before = current
          current= current.next
      return True

  # Return True if a list is empty or False otherwise
  def is_empty (self): 
      if self.length == 0:
          return True
      else:
          return False

  # Merge two sorted lists and return new list in ascending order
  # do not change the original lists
  def merge_list (self, other): 
      new_list = LinkedList()
      current = self.first
      while current:
          new_list.insert_in_order(current.data)
          current = current.next
      #Current will be established to the second list then added here
      current = other.first
      while current:
          #Insert in order function keeps the order in ascending
          new_list.insert_in_order(current.data)
          current = current.next
      return new_list

  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
      if self.length == 0 and other.length == 0:
          #If length is 0 best case - return 0
          return True
      first_current = self.first
      second_current = other.first
      
      while first_current:
          if first_current.data != second_current.data:
              #Return false if a value is not equal to each other. 
              return False
          first_current = first_current.next
          second_current = second_current.next
          if first_current.next == None or second_current.next == None:
              if second_current.next == None and first_current.next == None:
                  return True
              return False
      return True

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  # do not change the original list
  def remove_duplicates (self):
      occured_values = []
      new_list = LinkedList()
      
      if self.length == 0:
          #Best case
          return new_list
      elif self.length == 1:
          #No duplicates in this length
          new_list.insert_last(self.first)
          return new_list
      else:
          current = self.first
          while current:
              if current.data not in occured_values:
                  #Append the value into the occured list so we can check later
                  occured_values.append(current.data)
                  new_list.insert_last(current.data)
              current = current.next
      return new_list


  def combined_list(self, other):
      combined = LinkedList()
      if self.length == 0 and other.length == 0:
          return combined
      curr1 = self.first
      curr2 = other.first
      while curr1 and curr2:
          combined.insert_last(curr1.data + curr2.data)
          curr1 = curr1.next
          curr2 = curr2.next
      while curr1:
          combined.insert_last(curr1.data)
          curr1 = curr1.next
      while curr2:
          combined.insert_last(curr2.data)
          curr2 = curr2.next
      return combined

          

def main():
  # will be using print statements instead of assert as allowed by piazza note #647

  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.
  first = LinkedList()
  for x in range(20):
      first.insert_first(x)
  print(first)
  

  # Test method insert_last()
  first.insert_last(25)
  first.insert_last(30)
  print(first)

  # Test method insert_in_order()
  first.insert_in_order(20)
  print(first)

  # Test method get_num_links()
  print(first.get_num_links())

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there
  print(first.find_unordered(50))
  print(first.find_unordered(25)) 

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there
  first = first.sort_list()
  print(first.find_ordered(5))
  print(first.find_ordered(100))
  
  
  # Test method delete_link()
  # Consider two cases - data is there, data is not there 
  first.delete_link(7)
  print(first)
  first.delete_link(100)
  print(first)
  
  
  # Test method copy_list()
  second = first.copy_list()
  print(second)

  # Test method reverse_list()
  third = first.reverse_list()
  print(third)

  # Test method sort_list()
  fourth = third.sort_list()
  print(fourth)

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted
  print(third.is_sorted())
  print(fourth.is_sorted())

  # Test method is_empty()
  fifth = LinkedList()
  print(fourth.is_empty())
  print(fifth.is_empty())

  # Test method merge_list()
  sixth = LinkedList()
  for x in range(62,69):
      sixth.insert_last(x)
  seventh = LinkedList()
  for x in range(15,25):
      seventh.insert_first(x)
  eighth = sixth.merge_list(seventh)
  print(eighth)

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal
  ninth = third.copy_list()
  print(ninth.is_equal(sixth))
  print(first.is_equal(second))
  
  
  # Test remove_duplicates()
  tenth = LinkedList()
  for x in range(15,25):
    tenth.insert_last(x)
  for x in range(20,30):
    tenth.insert_last(x)
  final = tenth.remove_duplicates()
  print(final)
  
  

  #ADD TWO LISTS TOGETHER
  add1 = LinkedList()
  add2 = LinkedList()
  for num in range(5,15):
      add1.insert_last(num)
  for num in range(20,31):
      add2.insert_last(num)
  combined = add1.combined_list(add2)
  print(combined)

  return

if __name__ == "__main__":
  main()