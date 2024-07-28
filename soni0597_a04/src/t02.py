"""
------------------------------------------------------------------------
Assignment 4, Task 2
------------------------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = '2024-02-03'
------------------------------------------------------------------------
"""

from Queue_circular import Queue

queue1 = Queue()
queue2 = Queue()
for element in [1, 2, 3, 4, 5]:
    queue1.insert(element)
    queue2.insert(element)
if queue1.__eq__(queue2):
    print("queue1 and queue2 are equal.")
else:
    print("queue1 and queue2 are not equal.")
queue2.remove()
queue2.insert(6)
if queue1.__eq__(queue2):
    print("queue1 and queue2 are equal.")
else:
    print("After modification, queue1 and queue2 are not equal.")