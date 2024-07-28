"""
------------------------------------------------------------------------
Assignment 3, Task 5
------------------------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = "2024-01-27"
------------------------------------------------------------------------
"""

from functions import is_palindrome_stack

string = "A man, a plan, a canal, Panama!"

print(f"Is the string '{string}' a palindrome: ", end = "")
print(is_palindrome_stack(string))