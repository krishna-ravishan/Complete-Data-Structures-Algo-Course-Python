# Permutation

def permutation(list1, list2):
    if len(list1) != len(list2):
        return False
    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False
    
print(permutation([1,3,2,4,5], [1, 2, 3, 4, 5]))