#  File: WordSearch.py

#  Description: This project solves cross words.

#  Student Name: Michael Pham

#  Student UT EID: mp46987

#  Partner Name: 

#  Partner UT EID: 

#  Course Name: CS 313E 

#  Unique Number: 51125

#  Date Created: January 4th 

#  Date Last Modified: January 4th 

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input ( ):
    word_grid_size = int(sys.stdin.readline()) # Get grid size from input
    word_grid = []
    sys.stdin.readline() # read over blank line
    
    # iterate over each line of grid and add to 2d list
    for i in range(word_grid_size):
        line = sys.stdin.readline()
        word_grid.append(line.split())
    
    sys.stdin.readline() # read over blank line

    # retrieve word list and add to 1d list
    word_list_size = int(sys.stdin.readline())
    word_list = []
    for i in range(word_list_size):
        word_list.append(sys.stdin.readline().strip()) # get rid of newline char

    return word_grid, word_list

# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching 
#         or (0, 0) if the word does not exist in the grid
def find_word (grid, word):
    directions = [[1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1], [0,-1], [1,-1]] # list different directions the word can be found in
    word_grid_size = len(grid)
    for x in range(word_grid_size): # iterate through the 2d array
        for y in range(word_grid_size):
            if grid[x][y] == word[0]: # if a match is found, iterate through possible directions 
                for d in directions:
                    temp_x = x
                    temp_y = y
                    i = 0
                    # make sure the current coordinate is in bounds and matches the word letter
                    while temp_x >= 0 and temp_y >= 0 and temp_x < word_grid_size and temp_y < word_grid_size and grid[temp_x][temp_y] == word[i]: 
                        if i == len(word)-1: # return successful coordinate if at end of string
                            return (x+1, y+1) # account for indexing difference
                        temp_x += d[0]
                        temp_y += d[1]
                        i += 1
                        

    return (0, 0)

def main():
    # read the input file from stdin
    word_grid, word_list = read_input()

    # find each word and print its location
    for word in word_list:
        location = find_word (word_grid, word)
        print (word + ": " + str(location))

if __name__ == "__main__":
    main()
