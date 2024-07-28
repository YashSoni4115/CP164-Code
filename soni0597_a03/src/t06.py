"""
------------------------------------------------------------------------
Assignment 3, Task 6
------------------------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = "2024-01-27"
------------------------------------------------------------------------
"""

from functions import postfix

string = "4 5 + 12 * 2 3 * -"

print(f"For the postfix '{string}', the answer is: ", end = "")
print(postfix(string))