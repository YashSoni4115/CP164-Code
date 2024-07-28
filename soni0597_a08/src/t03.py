"""
-------------------------------------------------------
[assignment 8, Task 3]
-------------------------------------------------------
Author:  Yash Soni
ID:         169060597
Email:   soni0597@mylaurier.ca
__updated__ = "2024-03-11"
-------------------------------------------------------
"""
# Imports
from BST_linked import BST
from functions import fill_bst, letter_table, do_comparisons, comparison_total

DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"


bst2 = BST()


fill_bst(bst2, DATA2)

fv = open("miserables.txt", "r", encoding="utf-8")
do_comparisons(fv, bst2)
t2 = comparison_total(bst2)

letter_table(bst2)