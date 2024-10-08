# Min cost to last cell

def findMinCost(twoDArray, row, col):
    if row == -1 or col == -1:
        return float("inf")
    if row == 0 and col == 0:
        return twoDArray[0][0]
    else:
        op1 = findMinCost(twoDArray, row-1, col)
        op2 = findMinCost(twoDArray, row, col-1)
        return twoDArray[row][col] + min(op1, op2)
    
arr = [
    [4, 6, 2, 5, 2],
    [6, 7, 27, 1, 2],
    [1, 6, 2, 5, 2],
    [1, 6, 2, 5, 2],
    [4, 1, 1, 1, 1],
]

print(findMinCost(arr, 4, 4))