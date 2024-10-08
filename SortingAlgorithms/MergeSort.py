# Merge Sort: We divide the array into sub arrays until they're atomic. After that while merging we sort the individual elements
# Merge function merges two subarrays of customList
def merge(customList, left, mid, right):
    # Number of elements of first and second sub array
    n1 = mid - left + 1
    n2 = right - mid

    # Create two temp arrays
    leftArray = [0] * n1
    rightArray = [0] * n2

    # Copy elements into respective arrays
    for i in range(0, n1):
        leftArray[i] = customList[left + i]
    for j in range(0, n2):
        rightArray[j] = customList[mid + 1 + j]

    # Now while merging we've to sort the sub lists
    i = 0 # Initial index of first sub array
    j = 0 # Initial index of second sub array
    k = left # Initial index of merged sub array
    while i < n1 and j < n2:
        if leftArray[i] <= rightArray[j]:
            customList[k] = leftArray[i]
            i += 1
        else:
            customList[k] = rightArray[j]
            j += 1
        k += 1

    # Copy the remaining elements of leftArray, if any
    while i < n1:
        customList[k] = leftArray[i]
        i += 1
        k += 1

    # Copy the remaining elements of rightArray, if any
    while j < n2:
        customList[k] = rightArray[j]
        j += 1
        k += 1    

def mergeSort(customList, left, right):
    if left < right:
        m = (left + right ) // 2
        mergeSort(customList, left, m) # O(N/2)
        mergeSort(customList, m + 1, right) # O(N/2)
        merge(customList, left, m, right) # O(N)
    return customList

customList = [1, 5, 2, 6, 9, 10, 19, -1, 4]
mergeSort(customList, 0, len(customList) - 1)
print(customList)

# Time complexity: O(NlogN)
# Space Complexity: O(N)

# Use when you need stable sort and average expected time is O(nlogn)

# Avoid when space is a concern