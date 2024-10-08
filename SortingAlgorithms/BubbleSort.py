# BUBBLE SORT
# A.K.A Sinking Sort
# We repeatedly compare each pair of adjacent items and swap them if they are in the wrong order
# Space Complexity: O(1)
# Time Complexity: O(N^2)

def bubbleSort(myList):
    for i in range(len(myList) - 1):
        for j in range(len(myList) - i - 1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
    print(myList)

myList = [432, 6, 2, 78, 24, 22]
bubbleSort(myList)

# When to use bubble sort?
# When input is already sorted
# When space is a concern
# Easy to implement

# Dont use bubble sort when time ios a concern as its time complexity is poor/high