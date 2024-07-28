"""
-------------------------------------------------------
Lab 4, Task 3
-------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = '2024-02-03'
-------------------------------------------------------
"""

from List_array import List

my_list = List()

print("Appending elements to the list...")
my_list.append(1)
my_list.append(3)
my_list.append(4)
print(f"List after appends: {[value for value in my_list]}") 

print("\nInserting an element at index 1...")
my_list.insert(1, 2)
print(f"List after insert: {[value for value in my_list]}") 

print("\nRemoving the element '4'...")
removed_value = my_list.remove(4)
print(f"Removed value: {removed_value}") 
print(f"List after removal: {[value for value in my_list]}")  

print("\nAttempting to remove a non-existent element '5'...")
result = my_list.remove(5)
print(f"Result of removal: {result}") 
print(f"List after failed removal attempt: {[value for value in my_list]}") 