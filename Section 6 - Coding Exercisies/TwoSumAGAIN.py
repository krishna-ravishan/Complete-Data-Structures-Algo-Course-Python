def pair_sum(myList, sum):
    # TODO
    myList = [(index, value) for index, value in enumerate(myList)]
    myList.sort(key= lambda x: x[-1])
    left = 0
    right = len(myList) - 1
    new_list = []
    while left < right:
        if myList[left][1] + myList[right][1] == sum:
            new_list.append(f'{myList[left][0]}+{myList[right][0]}')
        elif myList[left][1] + myList[right][1] < sum:
            i += 1
        else: 
            j += 1
    return new_list

print(pair_sum([1, 2, 8, 3, 1], 9))