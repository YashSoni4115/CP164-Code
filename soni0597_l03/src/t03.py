"""
------------------------------------------------------------------------
Lab 3, Task 3
------------------------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = "2024-01-26"
------------------------------------------------------------------------
"""

from Queue_array import Queue
from utilities import queue_test
from utilities import queue_to_array
from utilities import array_to_queue

q = Queue()

source = [1, 2, 3, 4]
print("Original source array:", source)

array_to_queue(q, source)
print("Source array after populating queue:", source)
print("Queue after populating from source:", [val for val in q])

target = []
queue_to_array(q, target)
print("Queue after transferring to target array:", [val for val in q])
print("Target array after receiving queue contents:", target)

print("\nTesting queue operations:")
test_data = [60, 70, 80, 90, 100]
queue_test(test_data)