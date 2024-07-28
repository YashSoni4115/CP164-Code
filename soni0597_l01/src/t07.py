"""
-------------------------------------------------------
Lab 1, Task 7
-------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = '2024-01-12'
-------------------------------------------------------
"""

from Food_utilities.Food_utilities import get_vegetarian, read_foods
from Food import Food

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

veggies = get_vegetarian(foods)

for each in veggies:
    print(each)
    print()