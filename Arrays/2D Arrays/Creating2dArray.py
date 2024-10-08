import numpy as np

arr = np.array([
    [11, 15, 10, 6],
    [10, 14, 11, 5],
    [12, 17, 12, 8],
    [15, 18, 14, 9]
], dtype=int)

print(arr)
print(arr[1, 2])

# Add column: axis = 1
new = np.insert(arr, 0, [[1, 2, 3, 4]], axis=1)
print(new)

# Add row: axis = 0
new1 = np.insert(arr, 0, [[1, 2, 3, 4]], axis=0)
print(new1)

# Append row
new2 = np.append(arr, [[1, 2, 3, 4]], axis=0)
print(new2)