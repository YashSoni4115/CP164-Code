"""
-------------------------------------------------------
Lab 4, Task 7
-------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = '2024-02-03'
-------------------------------------------------------
"""

from Food_utilities import read_foods
from utilities import list_test
from List_array import List

llist = List()

fh = open("foods.txt", "r", encoding="utf-8")

foods = read_foods(fh)

for each in foods:
    llist.append(each)
    
list_test(llist)