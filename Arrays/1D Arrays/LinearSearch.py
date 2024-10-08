from array import *

arr1 = array('i', [1,2,3,4])

def linear_search(array, target):
    for i in range(0, len(array)):
        if array[i] == target:
            return i
    return -1
 
key_index = linear_search(arr1, 3)
print(key_index)