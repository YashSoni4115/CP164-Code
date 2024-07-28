"""
------------------------------------------------------------------------
Assignment 2, Task 1
------------------------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = "2024-01-19"
------------------------------------------------------------------------
"""

from Food_utilities import read_foods, by_origin, food_table

fh = open("foods.txt", "r")

foods = read_foods(fh)

Can_foods = by_origin(foods, 0)

print("Showing all Canadian foods:\n")

food_table(Can_foods)