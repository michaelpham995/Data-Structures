#  File: TestCipher.py

#  Description: This is a series of encrytpion. The first being the rail fence
# method that takes in a string and key. Then what's returned is the reordered version
# based on the number of rows. After this we decode it and have a simple string 
# simplifier. Then we have the vigenere code that creates a pass phrase
#and ASCII code. 

#  Student's Name: Michael Pham

#  Student's UT EID: mp46987
 
#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):
    
    rail_fence_cipher = ''
    bounce = key * 2 -2 #This tells us when the cipher will be moving directions
    for row in range(key):
        position = 0
        
        if row == 0:
            while position < len(strng):
                rail_fence_cipher += strng[position]
                position += bounce
        elif row == key - 1:
            position = row
            while position < len(strng):
                rail_fence_cipher += strng[position]
                position += bounce
        else:
            left = row
            right = bounce - row
            while left < len(strng):
                rail_fence_cipher += strng[left]
                if right < len(strng):
                    rail_fence_cipher += strng[right]
                left += bounce
                right += bounce
                        
    return(rail_fence_cipher)
                
                    
                
#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):
        
    rail_fence = [[] for a in range(key)]
    row = 0
    character = 1
    for unit in strng:
        rail_fence[row].append(unit)
        row += character
        if row == key-1 or row == 0:
            character = -character

    codedfence = [[] for a in range(key)]
    i = 0
    l = len(strng)
    s = list(strng)
    for r in rail_fence:
        for j in range(len(r)):
            codedfence[i].append(s[0])
            s.remove(s[0])
        i += 1

    rail = 0
    character  = 1
    decoded_string = ''
    for a in range(l):
        decoded_string += codedfence[rail][0]
        codedfence[rail].remove(codedfence[rail][0])
        rail += character

        if rail == key-1 or rail == 0:
            character = -character

    return decoded_string
    
    
#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
    
    letters_only = ''
    x = strng
    for a in x:
        if a.isalpha():
            letters_only += a
    x = letters_only.lower()
    
    return x	# placeholder for the actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 

def encode_character (p, s):
    
    p_phrase = ord(p) - ord('a')
    s_phrase = ord(s) - ord('a')
    return chr(ord('a') + (p_phrase + s_phrase) % 26)  #26 letter ASCII code

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
    
    index_p = ord(p) - ord('a')
    s_phrase = ord(s) - ord('a')
    return chr(ord('a') + abs(s_phrase - index_p + 26) % 26)	#26 letter ASCII code

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
    
    encoded_phrase = ""
    length = len(phrase)
    for a in range(len(strng)):
        encoded_phrase += encode_character(phrase[a % length], strng[a])
    return ("".join(encoded_phrase))


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
    
    decoded_phrase = ""
    length = len(phrase)
    for b in range(len(strng)):
        decoded_phrase += decode_character(phrase[b % length], strng[b])
    return ("".join(decoded_phrase))


def main():
    
    x = rail_fence_encode('jtanisabitch', 12)
    print(x)
    y = rail_fence_decode(x, 4)
    print(y)
    z = filter_string('THi3s')
    print(z)

  # read the plain text from stdin

  # read the key from stdin

  # encrypt and print the encoded text using rail fence cipher

  # read encoded text from stdin
   
  # read the key from stdin

  # decrypt and print the plain text using rail fence cipher

  # read the plain text from stdin

  # read the pass phrase from stdin

  # encrypt and print the encoded text using Vigenere cipher

  # read the encoded text from stdin

  # read the pass phrase from stdin

  # decrypt and print the plain text using Vigenere cipher

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
