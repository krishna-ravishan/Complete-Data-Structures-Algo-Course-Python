# Zero One Knapsack using DP

class Item:
    def __init__(self, profit, weight) -> None:
        self.profit = profit
        self.weight = weight
        self.memo = {}

def zeroOneKnapsack(items, capacity, currentIndex, memo):
    if capacity <= 0 or currentIndex <0 or currentIndex >= len(items):
        return 0
    elif items[currentIndex].weight <= capacity:
        if (currentIndex, capacity) not in memo:
            profit1 = items[currentIndex].profit + zeroOneKnapsack(items, capacity - items[currentIndex].weight, currentIndex+1, memo)            
            profit2 = zeroOneKnapsack(items, capacity, currentIndex+1, memo)
            memo[(currentIndex, capacity)] = max(profit1, profit2)
        return memo[(currentIndex, capacity)]
    else:
        return 0
    
# Bottom Up Approach (Don't Understand RN. Check it out later.)

def zeroOneKnapsackBU(profits, weights, capacity):
    if capacity <= 0 or len(profits) == 0 or len(weights) != len(profits):
        return 0
    numberOfRows = len(profits) + 1
    dp = [[None for i in range(capacity+2)] for j in range(numberOfRows)]
    for i in range(numberOfRows):
        dp[i][0] = 0
    for i in range(capacity+1):
        dp[numberOfRows-1][i] = 0
    for row in range(numberOfRows-2, -1, -1):
        for column in range(1,capacity+1):
            profit1 = 0
            profit2 = 0
            if weights[row] <= column:
                profit1 = profits[row] + dp[row + 1][column - weights[row]]
            profit2 = dp[row + 1][column]
            dp[row][column] = max(profit1, profit2)
    return dp[0][capacity]
    
mango = Item(31, 3) 
apple = Item(26, 1) 
banana = Item(17, 2) 
orange = Item(72, 5)

items = [mango, apple, orange, banana]

print(zeroOneKnapsack(items, 7, 0, {}))