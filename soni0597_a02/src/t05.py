"""
------------------------------------------------------------------------
Assignment 2, Task 5
------------------------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = "2024-01-19"
------------------------------------------------------------------------
"""

from Food_utilities import read_foods, food_table, food_search

fh = open("foods.txt", "r")

foods = read_foods(fh)

searched_foods = food_search(foods, 1, 200, True)

print("Showing all vegetarian Chinese foods with a maximum of 200 calories:\n")

food_table(searched_foods)