myDict = {
    'name': 'Krishna',
    'age': 21,
    'address': 'Navi Mumbai' 
}

def traverseDict(dictionary):
    for key in dictionary:
        print(key, dictionary[key])

traverseDict(myDict)

def searchDict(dictionary ,target):
    for key in dictionary:
        if dictionary[key] == target:
            # print(key)
            print("Target exists with key value "+key)

searchDict(myDict, 'Krishna')

# Delete an element from a dictionary
del myDict['address'] #TC: O(1) because it involves hash table operation
print(myDict)

# We can also use pop but it requires one argument that is the key

myDict.pop('age')
print(myDict)