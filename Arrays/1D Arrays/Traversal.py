from array import *

arr1 = array('i', [1,2,3,4,5,6])
arr2 = array('d', [1.3,1.5,1.6])

# print(arr1)
# print(arr2)

# arr1.insert(2, 9)
# print(arr1)

# def traverseArray(array): 
#     for i in array:
#         print(i)

# traverseArray(arr1)

## Accessing an Array element

def accessElement(array, index):
    if index > len(array):
        print("Index out of range!")
    else:
        print(array[index])

accessElement(arr1, 3)
accessElement(arr1, 7)