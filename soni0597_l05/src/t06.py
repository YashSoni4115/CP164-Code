"""
------------------------------------------------------------------------
Lab 5, Task 6
------------------------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = '2024-02-09'
------------------------------------------------------------------------
"""
from functions import bag_to_set

old_list = [4, 5, 3, 4, 5, 2, 2, 4]

new_list = bag_to_set(old_list)

print(f"The list {old_list} clears out to {new_list}")