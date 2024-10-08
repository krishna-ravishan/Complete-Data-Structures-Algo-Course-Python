import numpy as np

arr = np.array([
    [11, 15, 10, 6],
    [10, 14, 11, 5],
    [12, 17, 12, 8],
    [15, 18, 14, 9]
], dtype=int)

def accessElements(array, rowIndex, columnIndex):
    if rowIndex >= len(array) or columnIndex >= len(array[0]):
        print("Index out of range")
    else:
        print(array[rowIndex][columnIndex])

accessElements(arr, 1, 3)