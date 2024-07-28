"""
-------------------------------------------------------
Lab 7, Task 6
-------------------------------------------------------
Author:  Yash Soni
ID:      169060597
Email:   soni0597@mylaurier.ca
__updated__ = "2024-02-29"
-------------------------------------------------------
"""
from List_linked import List

original_list = List()
for value in range(1, 6):
    original_list.append(value)

print("Original List:")
current = original_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()

original_list.reverse_r()

print("Reversed List:")
current = original_list._front
while current is not None:
    print(current._value, end=" ")
    current = current._next
print()