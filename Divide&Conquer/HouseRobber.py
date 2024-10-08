# House Robber Problem
# Given N number of houses along the street with some amount of money, adjacent houses cannot be stolen from. Find the maximum amount that can be stolen from these houses.

# Can break it down into two sub problems. Like Option 1 = 6 + f(5) and option 2 = 0 + f(6). We take the maximum of these two options. 

# This works using the following algorithm

# maxValueHouse(houses, currentHouse):
#     if currentHouse > len of houses:
#         return 0
#     else:
#         stealFirstHouse = currentHouse + maxValueHouse(houses, currentHouse + 1)
#         skipFirstHouse = maxValueHouse(houses, currentHouse + 1)
#         return max(stealFirstHouse, skipFirstHouse)

# Implementation

def maxValueHouse(houses, currentHouse):
    if currentHouse >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentHouse] + maxValueHouse(houses, currentHouse + 2)
        skipFirstHouse = maxValueHouse(houses, currentHouse + 1)
        return max(stealFirstHouse, skipFirstHouse)
    
nums = [1,2,3,1]
print(maxValueHouse(nums, 0))