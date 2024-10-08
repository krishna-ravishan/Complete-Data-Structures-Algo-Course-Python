# House Robber using DP

def houseRobber(houses, currentHouse, memo):
    if currentHouse >= len(houses):
        return 0
    if currentHouse not in memo:
        stealFirstHouse = houses[currentHouse] + houseRobber(houses, currentHouse+2, memo)
        skipFirstHouse = houseRobber(houses, currentHouse+1, memo)
        result = max(stealFirstHouse, skipFirstHouse)
        memo[currentHouse] = result
    return memo[currentHouse]

houses = [1,2,3,1]
print(houseRobber(houses, 0, {}))

# Bottom Up Approach

def houseRobberBU(houses, currentIndex):
    tempAr = [0] * (len(houses)+2)
    for i in range(len(houses)-1, -1,-1):
        tempAr[i] = max(houses[i]+tempAr[i+2], tempAr[i+1])
    return tempAr[0]

print(houseRobberBU(houses, 0))