# BINARY SEARCH (FASTER THAN LINEAR SEARCH)
# O(logN) Time complexity O(1) Space Complexity
# Only works for sorted arrays

# Two ways 1. Iterative 2. Recursive
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binarySearch(myList, target):
    start = 0
    end = len(myList) - 1
    middle = (start + end) // 2
    while start <= end:
        if myList[middle] == target:
            return middle
        elif target < myList[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = (start + end) // 2
    return -1

def binarySearchRecursive(myList, target, left, right):
    if left <= right:
        middle = (left + right) // 2
        if myList[middle] == target:
            return middle
        elif myList[middle] < target:
            return binarySearchRecursive(myList, target, middle + 1, right)
        else:
            return binarySearchRecursive(myList, target, left, middle - 1)
    else:    
        return -1

print(binarySearch(myList, 9))
print(binarySearchRecursive(myList, 1, 0, len(myList) - 1))
