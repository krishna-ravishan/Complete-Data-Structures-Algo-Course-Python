# 1. Both data structures are mutable
# 2. Both can be indexed and iterated through
# 3. They both can be slices 

# Arrays are optimised for arithmetic operations
import numpy as np

anyArray = np.array([1, 2, 3, 4, 5])
myList = [1, 2, 3, 4, 5]

# Difference is that you cannot perform arithmetic operations on lists

print(anyArray/2)
# print(myList/2) Results in error

#  In array the datatype of elements has to be the same
# If array has string then it converts rest of the integers to strings as well

