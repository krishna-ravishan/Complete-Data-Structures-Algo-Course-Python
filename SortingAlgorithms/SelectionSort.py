# Selection Sort
# Based on the idea of finding the minimum element and move it to the sorted part of the array to make the unsorted part sorted

# Advantage: It performs well on small lists and its in pace sorting algorithm no extra space required.
# disadvantage: Poor efficiency when dealing with huge lists of python. Similar to bubble sort requires O(n^2). Hugely influenced by the initial ordering of the list

def selectionSort(myList):
    for i in range(len(myList)):
        min_index = i
        for j in range(i + 1, len(myList)):
            if myList[min_index] > myList[j]:
                min_index = j
        myList[i], myList[min_index] = myList[min_index], myList[i] 
    print(myList)

customList = [1, 5, 2, 6, 9, 10]
selectionSort(myList=customList)

# WHen can we use and avoid it?
# WHen we have insufficient memory and easy to implement
# WHen time is a concern avoid.