# The Two Sum Problem

# Write a program to find all pairs of integers whose sum is equal to the target

# Some vital questions to ask:
    # 1. Does the list contain positive integers only or negative integers as well?
    # 2. Do you need to return reverse pairs as well?
    # 3. What if pair repeats twice?
    # 4. Do we need to return distinct pairs only?
    # 5. What are the existing constraints on the size of the array?
# Improvise on complexity using two pointer method
def twoSum(nums, target):
    nums = [(index, value) for index, value in enumerate(nums)]
    nums.sort(key = lambda x: x[-1])
    left = 0
    right = len(nums) - 1
    while left < right:
        if nums[left][1] + nums[right][1] == target:
            print([nums[left][0], nums[right][0]])
            left += 1
        elif nums[left][1] + nums[right][1] < target:
            left += 1
        else: 
            right -= 1
my_list = [1, 3, 6, 1, 4 ,2 ,5, 2]
target = 5
twoSum(my_list, target)