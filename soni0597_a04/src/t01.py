"""
------------------------------------------------------------------------
Assignment 4, Task 1
------------------------------------------------------------------------
Author: Yash Soni
ID:     169060597
Email:  soni0597@mylaurier.ca
__updated__ = '2024-02-03'
------------------------------------------------------------------------
"""

from Queue_circular import Queue

queue = Queue()

list = [1,2,3,4,5]

print(f"Adding {list} into queue...")
for item in list:
    queue.insert(item)
    print(f"{item} inserted")
    
empty = queue.is_empty()
print(f"Is queue empty: {empty}")

full = queue.is_full()
print(f"Is queue full: {full}")

first_element = queue.peek()
print(f"The first element is: {first_element}")

removed_element = queue.remove()
print(f"Removed element {removed_element} from the queue.")

print(f"The queue has {len(queue)} elements.")

another_queue = Queue()
for i in range(5):
    another_queue.insert(i)

if queue == another_queue:
    print("The queues are equal.")
else:
    print("The queues are not equal.")

print("Iterating over the queue:")
for value in queue:
    print(value)