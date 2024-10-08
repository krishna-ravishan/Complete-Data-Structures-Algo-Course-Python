# 1. For single for loop, you've O(n) Time complexity

def foo(array):
    sum = 0
    product = 1

    for i in array:
        sum += i

    for i in array:
        product *= i

    print("Sum = "+str(sum)+", Product = "+str(product))

# This takes Linear time complexity which is O(n)

# 2. For two nested for loops you've time complexity O(n^2)

# 3. Still in worse case scenario, it's going to be O(n^2)

# 4. If size of array 1 = n and array 2 = m and they are nested then time complexity will be O(mn)

# 5. Two different arrays and another loop running o times (where 0 is constant) then its going to be O(mn)

# 6. For one for loop where increment or decrement is a division or multiplication of 2 then timecomplexity is going to be O(logn)

# 7. O(N) Equivalents

    # O (N + P), where P < N/2
    # O(2N)
    # o(N + LOGN)
    # O(N + NLogN) X is not equivalent as NlogN is greater than N 
    # O(N+M) X not qual to O(n)

# 8. 