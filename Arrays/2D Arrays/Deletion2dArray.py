import numpy as np

arr = np.array([
    [11, 15, 10, 6],
    [10, 14, 11, 5],
    [12, 17, 12, 8],
    [15, 18, 14, 9]
], dtype=int)

# Delete row from array
new_arr = np.delete(arr, 0, axis=0)
print(new_arr)
# Delete row from array
new_arr = np.delete(arr, 0, axis=1)
print(new_arr)