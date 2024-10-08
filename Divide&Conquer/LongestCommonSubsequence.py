# The longest common Subsequence

# The problem statement: S1 and S2 are given strings, find the length of the longest subsequence which is common to both strings.
# Subsequence: A sequence that can be driven from another sequence by deleting some elements without changing the order of them

# Example:
# s1 = "elephant"
# s2 = "erepat"
# Longest String = "eepat"

# Option 1 = 1 + f(2, 8: 2, 7)
# Option 2 = 0 + f(3, 8: 2, 7)
# Option 3 = 0 + f(2, 8: 3, 7)
# max(option1, option2, option3)

# Algorithm

# findLCS(s1, s2, index1, index2):
#     if index1 == len(s1) or index2 == len(s2):
#         return 0
#     if s1[index1] == s2[index12]:
#         return 1 + findLCS(s1, s2, index1+1, index2+1)
#     else:
#         op1 = findLCS(s1, s2, index1, index2+1)
#         op2 = findLCS(s1, s2, index1+1, index2)
#         return max(op1, op2)

def findLCS(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + findLCS(s1, s2, index1+1, index2+1)
    else:
        op1 = findLCS(s1, s2, index1, index2+1)
        op2 = findLCS(s1, s2, index1+1, index2)
        return max(op1, op2)
    
print(findLCS("elephant", "erepan", 0, 0))
