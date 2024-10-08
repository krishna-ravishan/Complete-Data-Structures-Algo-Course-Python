# BUCKET SORT
# Create buckets and distribute elements of array into buckets
# Sort buckets individually
# Merge buckets after sorting

# How many buckets to create and how will we distribute the elements

# First create buckets
# Number of buckets = round(sqrt(number of elements in array))
# Appropriate Bucket = cellValue * number of buckets / maxValue (Always round off to ceil)

def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >=0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return customList

import math

def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j*numberofBuckets/maxValue)
        arr[index_b-1].append(j)
    
    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i])
    
    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList

def negativeBucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    minValue = min(customList)
    rangeValue = maxValue - minValue + 1
    arr = []

    for i in range(numberofBuckets):
        arr.append([])
    
    for j in customList:
        index_b = math.floor((j - minValue) * numberofBuckets / rangeValue)
        arr[index_b].append(j)
    
    for i in range(numberofBuckets):
        arr[i] = insertionSort(arr[i])
    
    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
            
    return customList

customList = [1, 5, 2, 6, 9, 10, 1, 5, 7, 2]
customList_2 = [1, 5, 2, 6, -9, 10, 1, 5, 7, -2]
print(bucketSort(customList))  
print(negativeBucketSort(customList_2))  

# Time Complexity: O(n^2)
# Space Complexity: O(n) 

# When input data is uniformly distributed over range we can use bucket sort. Uniformally distributed means that there should not be great differenc es between the numbers in an array

# Do not use when space is a concern