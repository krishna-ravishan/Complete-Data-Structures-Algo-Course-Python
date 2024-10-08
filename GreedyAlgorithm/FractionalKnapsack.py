# Fractional Knapsack Problem

# Given a set of items, each with a weight and value, determine the number of each item to include in the collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

# First we need to take density of item. Value/Weight. Then order them according to density in decreasing order.

# Calculate the density or ratio for each item
# Sorting item based on this ratio
# take items with highest ratio sequentially until weight allows
# Add the next item fractionally as much as knapsack allows.

class Item:
    def __init__(self, weight, value) -> None:
        self.weight = weight
        self.value = value
        self.ratio = value/weight
        
def knapsackMethod(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    usedCapacity = 0
    totalValue = 0
    for i in items:
        if usedCapacity + i.weight <= capacity:
            usedCapacity +=  i.weight
            totalValue += i.value
        else:
            unusedWeight = capacity - usedCapacity
            value = i.ratio * unusedWeight
            usedCapacity += unusedWeight
            totalValue += value
        if usedCapacity == capacity:
            break
    print("Total value obtained: " + str(totalValue))
    
item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
cList = [item1, item2, item3]

knapsackMethod(cList, 50)

# Time complexity: O(ONLogN)
# Space complexity: O(1)

