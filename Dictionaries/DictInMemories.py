# A hash table is a way of doing key-value lookups. You store the values in an array, and then use a hash function to find the index of the array cell that corresponds to your key-value pair

# When dictionary assignments causes collisions, it adds it to the same index in the form a Linked List

# Insert/Update an element to the dictionary
myDict = {
    'name': 'Krishna',
    'age': 21
}

# If i want to change the value of age
myDict['age'] += 27
print(myDict)
# Add a new pair
myDict['address'] = 'Mumbai'
print(myDict)
