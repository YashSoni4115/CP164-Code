"""
------------------------------------------------------------------------
Assignment 3, Task 4
------------------------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = "2024-01-27"
------------------------------------------------------------------------
"""

from Stack_array import Stack

stack = Stack()

for a in [1,2,3,4,5]:
    stack.push(a)

stack.reverse()

for a in stack._values:
    print(a, end = " ")