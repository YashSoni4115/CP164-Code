"""
------------------------------------------------------------------------
Assignment 4, Task 6
------------------------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = '2024-02-03'
------------------------------------------------------------------------
"""

from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
for value in [10, 5, 20, 15, 5, 30]:
    pq.insert(value)

key = 15

higher_than_key, lower_or_equal_to_key = pq.split_key(key)

print("Original Priority Queue (should be empty):")
for value in pq:
    print(value, end=' ')
print()

print("Priority Queue with values higher than key:")
for value in higher_than_key:
    print(value, end=' ')
print()

print("Priority Queue with values lower than or equal to key:")
for value in lower_or_equal_to_key:
    print(value, end=' ')
print()