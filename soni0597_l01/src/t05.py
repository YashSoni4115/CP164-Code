"""
-------------------------------------------------------
Lab 1, Task 5
-------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = '2024-01-11'
-------------------------------------------------------
"""

from Food_utilities.Food_utilities import read_foods

fh = open("foods.txt", "r")

items = read_foods(fh)

for each in items:
    print(each)
    print()