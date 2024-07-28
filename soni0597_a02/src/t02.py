"""
------------------------------------------------------------------------
Assignment 2, Task 2
------------------------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = "2024-01-19"
------------------------------------------------------------------------
"""

from Food_utilities import read_foods, average_calories

fh = open("foods.txt", "r")

foods = read_foods(fh)

avg = average_calories(foods)

print(f"The average calories of the entire list is: {avg:.5}")