
#  File: ExpressionTree.py

#  Description: This program generates a binary tree utilizing expressions and returns the prefix and postfix expressions
#               and the answer for the expressions.

#  Student Name: Michael Pham 

#  Student UT EID:mp46987

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 51125

#  Date Created: 4/7/2022

#  Date Last Modified: 4/8/2022

from logging import root
from platform import node
import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def peek(self):
        #This will return the stop value of the stack to see what the answer we yield is 
        return self.stack[len(self.stack) - 1]

    def is_empty(self):
        return len(self.stack) == 0

    def length(self):
        #This is so we can pop the top of stack if we have remaining values at end of evaluation function.
        return len(self.stack)

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = Node(None)
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        input = expr.split()
        stack = Stack()
        curr = self.root
        for char in input:
            #Left paranthesis we move to the lChild
            if char == '(':
                curr.lChild = Node(None)
                stack.push(curr)
                curr = curr.lChild
                #If in operators we make an rChild and  update our node
            elif char in operators:
                #If in operators we bring it down into the tree
                curr.data = char
                curr.rChild = Node(None)
                stack.push(curr)
                curr = curr.rChild
                #If right paranthesis and empty stack we pop
            elif char == ')':
                if stack.length() != 0:
                    curr = stack.pop()
            else:
                curr.data = float(char)
                #Make sure all of our numbers are float so we can perform math operations
                curr = stack.pop()
                #We pop the value off the stack

    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        #tests to see if we have an operator as the data
        if aNode.data in operators:
            #we use number on the left and operator on the right
            return (self.math(self.evaluate(aNode.lChild), self.evaluate(aNode.rChild), aNode.data))
        return aNode.data
        #We return the answer in the form of aNode.data

    #This is a helper math function that gives definitions for each of the operators listed at beginning of program
    #Returns the two operands utilizing this function to solve the tree
    def math(self, oper1, oper2, operator):
        if operator == '+':
            return oper1 + oper2
        elif operator == '-':
            return oper1 - oper2
        elif operator == '*':
            return oper1 * oper2
        elif operator == '/':
            return oper1 / oper2
        elif operator == '//':
            return oper1 // oper2
        elif operator == '%':
            return oper1 % oper2
        elif operator == '**':
            return oper1 ** oper2

    def pre_fix_evaluate(self, aNode, pre_fix_list):
        #This helps make the evaluate function easier to perform
        if aNode:
            #Appending data to the prefix
            pre_fix_list.append(aNode.data)
            self.pre_fix_evaluate(aNode.lChild, pre_fix_list)
            #Add new node to the left
            self.pre_fix_evaluate(aNode.rChild, pre_fix_list)
            #Add new node to the right
        return pre_fix_list


    def post_fix_evaluate(self, aNode, post_fix_list):
        #This helps make the evaluate function easier to perform
        if aNode:
            self.post_fix_evaluate(aNode.lChild, post_fix_list)
            #Add new node to the left
            self.post_fix_evaluate(aNode.rChild, post_fix_list)
            #To the right
            post_fix_list.append(aNode.data)
            #Append data to list
        return post_fix_list

    
    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        pre_order_ans = ''
        #Below takes the list that we have so far
        pre_order_list = self.pre_fix_evaluate(aNode, [])
        for char in pre_order_list:
            if self.is_integer(char):
                #Call the output method that we created below to evaluate
                #This here will change out floats into integers for the output after math functions
                pre_order_ans += str(int(char)) + ' '
            else:
                pre_order_ans += str(char) + ' '
                #If not a float we simply add to the string
        return pre_order_ans


    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        post_order_ans = ''
        #Below takes the list that we have so far
        post_order_list = self.post_fix_evaluate(aNode, [])
        for char in post_order_list:
            if self.is_integer(char):
                #Call the output method that we created below to evaluate
                #This here will change out floats into integers for the output after math functions
                post_order_ans += str(int(char)) + ' '
            else:
                post_order_ans += str(char) + ' '
                #If not a float we simply add to the string
        return post_order_ans

    #This will help use calculate and output integers
    def is_integer(self, value):
        if isinstance(value, int):
            return True
        if isinstance(value, float):
            #If this is a float we need to change to an int for output
            return value.is_integer()
        else:
            #If we are not dealing with a number there is no need to do this function
            return False


            

# you should NOT need to touch main, everything should be handled for you
def main():
    #read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()