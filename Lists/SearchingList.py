# Searching for an element in a list
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# target = 50
# if target in my_list:
#     print(target)
# else:
#     print("Target is not in the list")

def searchList(my_list ,target):
    inList = True
    for element in my_list:
        if element == target:
            print(f"{target} is in the list")
            inList = True
        else:
            inList = False
    if not inList:
        print(f"{target} is not in the list")
searchList(my_list, 990)

# Linear Search (Check each element in List one by one)
def linearSearch(a_list, target):
    for i, value in enumerate(a_list):
        if value == target:
            return i
    return -1

print(linearSearch(my_list, 70))

# Time complexity of LinearSearch is O(n)