# Convert String Problem

# You are given a string s consisting of n characters.
# A move is defined as selecting characters of s and converting them to another.
# Return the minimum number of moves required so that all the characters of s are converted to another string s2. 
# You have delete, replace or insert operations.

# Algorithm looks like:

# findMinimum(s1, s2, index1, index2):
#     if index1 == len(s1):
#         return len(s2) -index2
#     if index2 == len(s2):
#         return len(s1) - index1
#     if s1[index] == s2[index]:
#         return findMinimum(s1, s2, index1+1, index2+1)

#     else:
#         deleteOp = 1 + findMinimum(s1, s2, index1, index2+1)
#         insertOp = 1 + findMinimum(s1, s2, index1+1, index2)
#         replaceOp = 1 + findMinimum(s1, s2, index1+1, index2+1)
#         return min(deleteOp, insertOp, replaceOp)
    
    
def findMinOperation(s1, s2, index1, index2):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1+1, index2+1)
    else:
        deleteOp = 1 + findMinOperation(s1, s2, index1, index2+1)
        insertOp = 1 + findMinOperation(s1, s2, index1+1, index2)
        replaceOp = 1 + findMinOperation(s1, s2, index1+1, index2+1)
        return min(deleteOp, insertOp, replaceOp)
    
print(findMinOperation("table", "tblqqq", 0, 0))