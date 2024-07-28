"""
------------------------------------------------------------------------
Assignment 3, Task 7
------------------------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = "2024-01-27"
------------------------------------------------------------------------
"""

from functions import stack_maze

maze = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'],
            'D':[], 'E':['F'], 'F':['G', 'H'], 'G':[], 'H':[]}

print(f"For the following maze '{maze}', the route is: ", end = "")
print(stack_maze(maze))