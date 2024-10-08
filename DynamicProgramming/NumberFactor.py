# Number Factor

# Problem statement: given N, find the number of ways to express N as a sum of 1, 3, 4.

# Implementation
# Top Down Approach
def tdNumberFactor(n, memo):
    if n in [0,1,2]:
        return 1
    elif n == 3:
        return 2
    else:
        res1=tdNumberFactor(n-1, memo)
        res2=tdNumberFactor(n-3, memo)
        res3=tdNumberFactor(n-4, memo)
        if (res1, res2, res3) not in memo:
            memo[n] = res1+res2+res3
    return memo[n]
memo = {}
print(tdNumberFactor(5, memo))

# Bottom Up Approach

def buNumberFactor(n, memo):
    tb = [1,1,1,2]
    # Iterate thru 2 to n+1 and then keep appending to list.
    for i in range(4, n+1):
        tb.append(tb[i-1]+tb[i-3]+tb[n-4])
    return tb[n]

memo = {}
print(buNumberFactor(5, memo))