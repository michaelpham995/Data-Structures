#  File: Tower.py

#  Description: This program calculates the number of moves it would take to move
#               the disks of the tower of Brahma

#  Student's Name: Michael Pham

#  Student's UT EID: mp46987

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number:  51125

#  Date Created: 3/6/2022

#  Date Last Modified: 3/7/2022
    
    
import sys

# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves (n):
    count = 0
    start = []
    spare1 = []
    spare2 = []
    end = []
    
    counter = 1
    #Best Case
    if n == 0:
        counter = 0
        return counter
    #Distinct case
    elif n == 1:
        counter = 1
        return counter
    #Distinct case
    elif n == 2:
        counter = 3
        return counter
    else:
        #Algorithm found
        subtract_count = 0
        n -= 2
        x = 2
        y = 3
        subtract = 0
        increaser = 2 ** x
        counter = 5
        a = n 
        #Utilizing a single wild loop to get throygh this
        while n > y:
            counter = counter + y * 2 ** x
            n -= x
            x += 1
            subtract += 1
            y += 1
        #Differences in the formula accounting
        if counter > 3:
            counter = counter + (n - subtract - 1) * 2 ** (x - 1) 
        return counter

        
        
        
#KEYS
#   First move top K disks from source to spare1
#   Move n - k - 1 disks to spare2
#   Move the largest disk from source to destination
#   Move n -k -1 disks from spare2 to destination
#   Finally move the top k disks from spare1 to destination

        

def main():
  # read number of disks and print number of moves
    for line in sys.stdin:
      line = line.strip()
      n = int (line)
      print (num_moves (n))
    print(num_moves(23))

if __name__ == "__main__":
  main()