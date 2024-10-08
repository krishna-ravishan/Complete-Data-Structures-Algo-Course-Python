# DICTIONARIES

# A dictionary is a collection of unordered changeable and indexed key-value pairs.

# Declare and initialize
myDict = {
    "Key": "Value",
    "Miller": "A person who works in a mill",
    "Programmer": "A person who writes computer programs"
}
print(myDict)
# Call a dictionary value using key's
print(myDict["Miller"])

# Dictionaries are based on hash tables
# We can also create a dictionary using a Dict() construct
my_dict = dict() # TC: O(1) SC: O(1)
print(my_dict)

eng_sp = dict(one="uno", two="dos", three="tres")
print(eng_sp)
print(eng_sp['one'])
eng_sp2 = {"one":"uno", "two":"dos", "three":"tres"}
print(eng_sp)
print(eng_sp['one'])
eng_sp3 = [("one","uno"), ("two","dos"), ("three","tres")]
print(eng_sp)
print(eng_sp['one'])
