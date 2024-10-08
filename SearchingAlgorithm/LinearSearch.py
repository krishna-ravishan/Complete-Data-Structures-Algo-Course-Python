myList = [1, 5, 3, 7, 2, 9, 2, 6]

# O(n) Time Complexity and O(1) Space Complexity
def linearSearch(myArray, target):
    for idx, num in enumerate(myArray):
        if num == target:
            return f"Element {target} exists at index {idx}"
    return "Element Does not Exist"

print(linearSearch(myList, 9))