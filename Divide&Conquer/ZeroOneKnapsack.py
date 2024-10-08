# Zero One Knapsack Problem

# Problem Statement: We're given the weights and profits of N items. We're supposed to find the maximum profit within given capacity of C. Items cannot be broken down.
# An example of this is buying fruits.

# In this case, we'll be using the divide and conquer algorithm. We break it down into 2 subproblems first, take option 1 with first item [profit of first item + f(2, 3, 4)] and then option 2 with second item [0 + f(2, 3, 4)]
# Algorithm looks like:

# zeroOneKnapsack(items, capacity, currentIndex):
#     if capacity==0 or currentIndex<0 or currentIndex > len(profits):
#         return 0
#     elif currentItemWeight <= capacity:
#         profit1 = currentItemProfit + zeroOneKnapsack(items, capacity - currentItemWeight, nextItem)
#         profit2 = zeroOneKnapsack(items, capacity-currentItemWeight, nextItem)
#         return max(profit1, profit2)
#     else:
#         return 0
        
# Implementation

class Item:
    def __init__(self, profit, weight) -> None:
        self.profit = profit
        self.weight = weight

def zeroOneKnapsack(items, capacity, currentIndex):
    if capacity <= 0 or currentIndex <0 or currentIndex >= len(items):
        return 0
    elif items[currentIndex].weight <= capacity:
        profit1 = items[currentIndex].profit + zeroOneKnapsack(items, capacity - items[currentIndex].weight, currentIndex+1)            
        profit2 = zeroOneKnapsack(items, capacity, currentIndex+1)
        return max(profit1, profit2)
    else:
        return 0
    
mango = Item(31, 3) 
apple = Item(26, 1) 
banana = Item(17, 2) 
orange = Item(72, 5)

items = [mango, apple, orange, banana]

print(zeroOneKnapsack(items, 7, 0))