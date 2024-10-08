#  HEAP SORT

# Insert data into binary heap tree
# Extract data from binary heap
# Best suited with array, does not work with linked list

# Binary heap is a binary tree with special properties. Any value of given node must be less than or equal to its children (min heap)
# Binary heap is a binary tree with special properties. Any value of given node must be greater than or equal to its children (max heap)

# For heap sort we'll use min heap

def heapify(customList, n, i):
    smallest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and customList[l] < customList[smallest]:
        smallest = l
    if r < n and customList[r] < customList[smallest]:
        smallest = r
    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        heapify(customList, n, smallest)
        
def heapSort(customList):
    n = len(customList)
    for i in range(int(n/2)-1, -1, -1):
        heapify(customList, n, i)
        
    for i in range(n-1, 0, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)
    customList.reverse()
    return customList
    
customList = [1, 5,2, 673, 7, 2, 76, 3]

print(heapSort(customList))

# Time complexity: O(NLogN)
# Space complexity: O(1)