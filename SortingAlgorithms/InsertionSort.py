# Insertion Sort
# Divide the given array into two parts
# Take the first element from unsorted array and find its correct position in sorted array
# Repeat until sorted array is empty

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >=0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    print(customList)

customList = [1, 5, 2, 9, 6, 10]
insertionSort(customList)