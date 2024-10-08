# newTuple = ('a', 'b', 'c', "d", 'e')

# for i in newTuple:
#     print(i, end=" ")

# def searchElement(some_tuple, target):
#     for i in some_tuple:
#         if i == target:
#             return some_tuple.index(i)
        
# print(searchElement(newTuple, 'c'))

# # Tuple operations and methods

# myTuple = (1, 4, 3, 2, 5)
# myTuple1 = (1, 2, 5, 7, 8, 2)

# # Concatenation
# print(myTuple + myTuple1)

# # * Operator
# print(myTuple * 4) # Repeats sequence of elements 4 times

# # in operator
# print(4 in myTuple)

# # Methods in tuple
# print(myTuple.count(2))
# print(myTuple.index(1))

# # Len function for tuples
# print(len(myTuple))
# print(max(myTuple))

# # TUPLES VS LIST
# # tuples are immutable and lists are mutable
# myTuple[1] = 2 # Results in error

# # tuples can be stored in lists and lists can be stored in tuples

# print([number for number in range(1, 201) if all(number % i != 0 for i in range(2, number))])
sum = 0
for i in range(1, 101):
    if i % 2 != 0:
        sum += i
print(sum)