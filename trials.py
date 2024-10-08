# def threeSum(nums):
#         n = len(nums)
#         i = 0
#         j = n - 1
#         results = []
#         counter = 0
#         while i < j:
#             for k in range(i + 1, j):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     results.append([nums[i], nums[j], nums[k]])
#                     counter += 1
#                 else:
#                     if counter % 2 == 0:
#                         j -= 1
#                         counter += 1
#                     else:
#                         i += 1
#                         counter += 1
#         return results

# nums = [-1,0,1,2,-1,-4]
# print(threeSum(nums))

# N = int(input())
# myList = []
# for i in range(N):
#     command_inp = input()
#     command_split = command_inp.split(" ", 1)
#     command = command_split
#     if len(command) > 1:
#         command = command_split[0]
#         elements = command_split[1]
#     if command == "append":
#         myList.append(int(elements))
#     elif command == "print":
#         print(myList)
#     elif command == "remove":
#         myList.remove(int(elements))
#     elif command == "sort":
#         myList.sort()
#     elif command == "pop":
#         myList.pop()
#     elif command == "reverse":
#         myList.sort(reverse=True)
#     elif command == "insert":
#         elements = elements.split(" ", 1)
#         pos = int(elements[0])
#         ele = int(elements[1])
#         myList.insert(pos, ele)
#     else:
#         print("Please enter correct command")

# def swap_case(s):
#     s = list(s)
#     for character in s:
#         if character.islower():
#             character = character.upper()
#         else:
#             character = character.lower()
#     return ''.join(s)

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)

def mySqrt(x: int) -> int:
        myList = [num for num in range(x + 1)]
        for i in range(int(len(myList)/2) + 1):
            if myList[i] * myList[i] == x:
                return int(myList[i])
            
print(mySqrt(8))