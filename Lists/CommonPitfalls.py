# Pitfall 1
myList = [2, 4, 3, 1, 5, 7]

# myList = myList.sort()

print(sorted(myList))

myList.append([10])
myList = myList + [10]

print(myList)