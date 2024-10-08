# Quick Sort
# The first thing we're doing is that we select a pivot number first. Then we're going to take all the elements in the list and make exchange operations with the pivot number.
# Swap number less than pivot number with first item greater than pivot number with the number
# Then at the end we swap the pivot number with the last number smaller than pivot number
# Now we find the location of the pivot in the sorted array.
# We again do the same for the part of the list less than pivot number and then the part greater than pivot number

# This function finds the position of the pivot in the ordered list and puts all elements less than pivot on the left and all elements greater to the right side.

# The pivot function has a pivot pointer, swap pointer and i pointer which will iterate through the list

def swap(customList, index1, index2):
    # temp = customList[index1]
    # customList[index1] = customList[index2]
    # customList[index2] = temp
    customList[index1], customList[index2] = customList[index2], customList[index1]

def pivot(customList, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if customList[i] < customList[pivot_index]:
            swap_index += 1
            swap(customList, swap_index, i)
        i += 1
    swap(customList, pivot_index, swap_index)
    return swap_index
    
def quickSort(customList, left, right):
    if left < right:
        pivot_index = pivot(customList, left, right)
        quickSort(customList, left, pivot_index)
        quickSort(customList, pivot_index + 1, right)
    return customList

customList = [3, 5, 0, 6, 2, 1, 4]
# print(pivot(customList, 0, len(customList) - 1))
# print(customList)
print(quickSort(customList, 0, len(customList) - 1))

# Time Complexity: O(NlogN)
# Space Complexity: O(N)