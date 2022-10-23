#  File: Reducible.py

#  Description: This program is designed to find the longest word that could be a word 
# for any length, if the word was reduced by a letter at a time.

#  Student Name: Michael Pham

#  Student UT EID: mp46987

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 3/21/22

#  Date Last Modified: 3/22/22
    
import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime ( n ):
  if (n == 1):
    return False

  limit = int (n ** 0.5) + 1
  div = 2
  while (div < limit):
    if (n % div == 0):
      return False
    div += 1
  return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word (s, size):
    hash_location = 0
    for x in range (len(s)):
        letter = ord (s[x]) - 96
        hash_location = (hash_location * 26 + letter) % size
    return hash_location

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size (s, const):
    return const - (hash_word(s, const))

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word (s, hash_table):
    
    index = hash_word(s, len(hash_table))
    if hash_table[index] == '':
        hash_table[index] = s
    else:
        #Establishing group for moving the index if filled
        group = 1
        step = step_size(s, 7)
        destination_index = (index + group * step) % len(hash_table)
        while (hash_table[destination_index]):
            #Run the while loop until we find an index that is not filled up
            destination_index = (index + group * step) % len(hash_table)
            group += 1
        #Establish the index
        hash_table[destination_index] = s
    
    
# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word (s, hash_table):
    
    index = hash_word(s, len(hash_table))
    if hash_table[index] == s:
        return True
    else:
        #Establishing group for moving the index if filled
        group = 1
        step = step_size(s, 7)
        destination_index = (index + group * step) % len(hash_table)
        while (hash_table[destination_index] and hash_table[destination_index] != s):
            #Run the while loop until we find an index that is not filled up
            destination_index = (index + group * step) % len(hash_table)
            group += 1
        #Establish the index
        if hash_table[destination_index] == s:
            #Return if the hash table equals the index needed
            return True
        else:
            #False if not
            return False

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible (s, hash_table, hash_memo):

    #Establish a false off the bat assuming that the word is not reducible before we run our test
    reducible = False
    if len(s) == 1:
        if s == 'i' or s == 'o' or s == 'a':
            if find_word(s, hash_memo) is False:
                #If not placed in the hash memo yet do so here
                insert_word(s, hash_memo)
            return True
    if find_word(s, hash_memo) == True:
        #If runs through test then return True
        return True
    else:
        for x in already_reduced(s):
            if x != 'i' and x != 'o' and x != 'a' and find_word(x, hash_table) == False:
                continue
            elif is_reducible(x, hash_table, hash_memo) is True:
                if find_word(s, hash_memo) is False:
                    insert_word(s, hash_memo)
                    #Set new reducible value here
                reducible = True
        return reducible 

        
def already_reduced(s):
    
    #Establish the already reduced list for the function
    reduced = []
    for x in range(len(s)):
        #Attaching the word together
        reduced.append(s[:x] + s[x + 1:]) 
    return reduced


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words (string_list):

    longest_word = 0
    #Create list
    longest_word_list = []
    for x in range(len(string_list)):
        addition = string_list[x]
        #Checking the next string in the list 
        checklength = len(addition)
        
        if checklength == longest_word:
            #Append if it is the longest word we have 
            longest_word_list.append(addition)
        elif checklength < longest_word:
            #Just continue because it does not matter to us if we are not dealing with longest word
            continue 
        elif checklength > longest_word:
            for y in range(len(longest_word_list)):
                longest_word_list.pop(0)
                #Remove to clear out the longest word list
            longest_word_list.append(addition)
            #Append if the word is longer than the current longest word 
            longest_word = checklength
    return longest_word_list


    

def main():
  # create an empty word_list
  word_list = []
  # read words from words.txt and append to word_list
  #x = open('words.txt', 'r')
  #for line in x:
    #line = line.strip()
  for line in sys.stdin:
    line = line.strip()    
    word_list.append (line)

  # find length of word_list
  length_list = len(word_list)

  # determine prime number N that is greater than twice
  # the length of the word_list
  greater_prime = length_list * 2 + 1
  while not is_prime(greater_prime):
      greater_prime += 2

  # create an empty hash_list
  hash_list = []

  # populate the hash_list with N blank strings
  for x in range(greater_prime):
      hash_list.append("")

  # hash each word in word_list into hash_list
  # for collisions use double hashing 
  for x in word_list:
      insert_word(x, hash_list)
      
  # create an empty hash_memo of size M
  # we do not know a priori how many words will be reducible
  # let us assume it is 10 percent (fairly safe) of the words
  # then M is a prime number that is slightly greater than 
  # 0.2 * size of word_list
  hash_memo = []
  M = int(length_list * 0.2)
  while not(is_prime(M)):
      M += 1
  
  # populate the hash_memo with M blank strings
  hash_memo = ['' for x in range(M)]

  insert_word('i', hash_memo)
  insert_word('o', hash_memo)
  insert_word('a', hash_memo)
  
  # create an empty list reducible_words
  reducible_words = []

  # for each word in the word_list recursively determine
  # if it is reducible, if it is, add it to reducible_words
  # as you recursively remove one letter at a time check
  # first if the sub-word exists in the hash_memo. if it does
  # then the word is reducible and you do not have to test
  # any further. add "the word to" the hash_m"emo.
  reducible_words = [x for x in word_list if is_reducible(x, hash_list, hash_memo) is True]
  
  # find the largest reducible words in reducible_words
  largest_reducible = get_longest_words(reducible_words)

  # print the reducible words in alphabetical order
  largest_reducible.sort()
  
  '''import time
  start = time.time()
  finish = time.time()
  print("Time: " + str(finish - start))'''
  # one word per line
  for x in largest_reducible:
      print(x)


if __name__ == "__main__":
  main()
