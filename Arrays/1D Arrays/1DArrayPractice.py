# Create array
from array import *

arr = array('i', [1, 2, 3, 4, 5])

# Traverse Array
def traverseArray(array):
    for i in array:
        print(i)

traverseArray(arr)

# Access individual elements through indexes
def accessElements(array, index):
    if index > len(array):
        print("Index out of range")
    else:
        print(array[index])

accessElements(arr, 4)

# Append a value to the array
print(arr)
arr.append(6)
print(arr)

# Insert a value
arr.insert(4, 10)
print(arr)

# Extend array using extend method
arr1 = array('i', [7, 8, 9])
arr.extend(arr1)
print(arr)

# Add items to array using from_list() method
arr.fromlist([7, 8, 9])
print(arr)

# Remove last element of array using pop()
popped_element = arr.pop()
print(popped_element)
print(arr)

# Fetch any element using index() method
def fetchElement(arr, index):
    print(arr.index(index))

fetchElement(arr, 3)

# Reverse a python array using reverse()
arr.reverse()
print(arr)

# Get array buffer information using buffer_info()
print(arr.buffer_info())

# Check the number of occurrences of an element using count() method
print(arr.count(8))

# Convert array to string using the tostring() method
a = arr.tobytes()
print(a)

# Convert array to a python list with the same elements using tolist() method
print(arr.tolist())

# Append a string to char array using frombytes() method
stringg = 'hello'
charay = array('b', [ord('h'), ord('e'), ord('l'), ord('l'), ord('o')])
print(charay)
