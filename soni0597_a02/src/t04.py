"""
------------------------------------------------------------------------
Assignment 2, Task 4
------------------------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = "2024-01-19"
------------------------------------------------------------------------
"""

from Food_utilities import read_foods, food_table

fh = open("foods.txt", "r")

foods = read_foods(fh)

food_table(foods)