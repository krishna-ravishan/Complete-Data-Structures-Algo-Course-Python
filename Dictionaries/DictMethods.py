# Clear method

myDict = {
    'name': 'Krishna',
    'age': 21,
    'address': "Navi Mumbai",
    'education': "Bachelors" 
}

# myDict.clear()
# myDict2 = myDict.copy()
# newDict = {}.fromkeys([1, 2, 3], 0)
# myDict.get('age', 21)
# myDict.items() returns a list of tuples consisting of key value pairs
# myDict.keys() Returns a list of all keys in a dictionary
# myDict.popitem() No need for parameters like key method
# myDict.setdefault('age', 22) # Returns the value of key in dictionary if there. If not, then sets the default value passed as parameter 
# myDict.update() takes a dictionary or tuple as parameter. Return is none.

print(myDict.update(({'a': 1, 'b': 2, 'c': 3})))
print(myDict)
