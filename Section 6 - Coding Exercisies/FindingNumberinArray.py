import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def linearSearch(array, target):
    for i in array:
        if target == array[i]:
            return i
        
index_of_target = linearSearch(arr, 18)
print(index_of_target)