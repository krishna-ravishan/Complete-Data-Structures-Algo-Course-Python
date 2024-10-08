# COIN CHANGE

# You're given coins of different denominations and total amount of money. Find the minimum number of coins that you need to make up the given amount.

# Infinite supply of denominations: [1, 2, 5, 10, 20, 50, 100, 1000]

# Find the biggest coin that is less than given total number
# Add coin to the result and subtract coin from total number
# If V is equal to zero:
#   then print result
# else:
# Repeat step 2 & 3

def coinChange(totalNumber, coins):
    N = totalNumber
    coins.sort()
    index = len(coins) - 1
    while True:
        coinValue = coins[index]
        if N >= coinValue:
            print(coinValue)
            N = N - coinValue
        if N < coinValue:
            index -= 1
        if N == 0:
            break

coins =  [1, 2, 5, 1001, 20, 50, 100, 1000, 2176]
coinChange(6249, coins)

# Time complexity: O(N)
# Space complexity: O(1)