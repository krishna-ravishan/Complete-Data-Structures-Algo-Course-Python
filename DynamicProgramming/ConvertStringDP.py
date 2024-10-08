# Convert String S1 to S2 

def findMinOperation(s1, s2, index1, index2, memo):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1+1, index2+1, memo)
    elif (index1, index2) not in memo:
        insertOp = 1 + findMinOperation(s1, s2, index1, index2+1, memo)
        deleteOp = 1 + findMinOperation(s1, s2, index1+1, index2, memo)
        replaceOp = 1 + findMinOperation(s1, s2, index1+1, index2+1, memo)
        memo[(index1, index2)] = min(deleteOp, insertOp, replaceOp)
    return memo[(index1, index2)]
print(findMinOperation("table", "tblqqq", 0, 0, {}))