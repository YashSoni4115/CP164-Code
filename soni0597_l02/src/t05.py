"""
-------------------------------------------------------
Lab 2, Task 2
-------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = '2024-01-19'
-------------------------------------------------------
"""

from Stack_array import Stack
from utilities import stack_test
from Food_utilities import read_food

s = Stack()

fh = open("foods.txt", "r", encoding="utf-8")

for line in fh:
    food = read_food(line)
    s.push(food)
    
stack_test(s)