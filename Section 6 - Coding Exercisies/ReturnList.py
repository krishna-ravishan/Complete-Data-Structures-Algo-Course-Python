def middle(lst):
    # TODO
    new = [number for index, number in enumerate(lst) if (index != 0) and (index != (len(lst)-1))]
    return new

myList = [1, 2, 3, 4]
print(middle(myList))