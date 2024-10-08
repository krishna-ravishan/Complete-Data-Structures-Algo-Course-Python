# An immutable sequence of python objects
# Tuples are also comparable and hashable - An object is said to be hashable if it remains the same during its lifetime

# How to create a tuple?

newTuple = ('a', 'b', 'c', "d", 'e')
# For single element in tuple , is required
newTuple1 = ('a',)
# We can also use tuple function
newTuple2 = tuple('abcde')

print(newTuple2)

# Accessing tuple elements
# Indexing starts with 0 from LHS and -1 form RHS
print(newTuple[0])

# Slicing
print(newTuple[2:4]) # including 2 till and excluding 4

#  But the difference is that we cannnot modify an element as tuples are immutable