#  RECURSION
# Recursion is a way of solving a problem by having a function call itself

# A simple example is Russian Dolls

# Performing the same operation multiple times with different inputs. In every step we try to make the solution smaller

# Base condition required to stop recursion else infinite loop occurs

# def RussianDolls(doll):
#     if doll == 1:
#         print("All dolls are open")
#     else:
#         RussianDolls(doll - 1)

# WHY RECURSION?
# Recursion can be simpler than normal methods
# Depends on situation where recursion works better than iteration and visa versa

# When to choose recursion?
# If you can break down problem into smaller sub problems
# The prominent use of recursion in data structure like trees and graphs
# Interviews
# Recursion used in many algorithms: divide and conquer, greedy and dynamic programming

# Take into account two conditions. The exit condition and base condition

# Recursive vs Iteration Solutions
# def power(base, exp):
#     if base == 0:
#         return 1
#     elif base < 0:
#         return 1/(base * power(base, exp + 1))
#     return base * power(base, exp-1)

# print(power(3, 6))

# Recursion uses stack memory

# Recursive vs Iterative Functions

# Recursion is easy to write compared to iterative function.
# Base condition required for Recursion and Termination condition required for iterative functions
# Recursive code on infinite recursion crashes system and iterative is cpu cycle consuming
# R is not space efficient but I is
# R is not time efficient but I is

# Use recursion when a problem can be broken down into sub-problems
# Use when we're fine with time and space overhead
# We need quick working sol instead of efficient one
# When we need to traverse a tree (Pre-order traversal)
# When we use memorization in recursion

# When to avoid it?
# If time and complexity matters. 
# Recursion is slow because it uses stack memory

# How to write recursion in 3 steps?

# FACTORIAL
# import sys
# sys.setrecursionlimit(10000)

# def fact(n):
#     assert n >= 0 and int(n) == n, 'The number must be a positive integer only!'
#     if n in [0, 1]:
#         return 1
#     else:
#         return n * fact(n - 1)
    
# print(fact(-1))

# Fibonacci Numbers

# def fib(n): # Take O(n) TC
#     assert n >= 0 and int(n) == n, "The number must be a positive integer only"
#     if n == 0:
#         return 0 # O(1)
#     elif n == 1:
#         return 1 # O(1)
#     else:
#         return fib(n - 1) + fib(n - 2) # O(n)

# print(fib(6))

# How to find time complexity of recursive code?
# For fib - O(braches^depth)
# Step 1: Recursive Case

# def sumOfDigits(n):
#     assert n >= 0 and int(n) == n, "Cannot be non positive integer or non integer"
#     if n == 0:
#         return 0
#     else:
#         return int(n % 10) + sumOfDigits(int(n/10))
    
# print(sumOfDigits(11))

# POWER
# def power(base, n):
#     if n == 0:
#         return 1
#     elif n < 0 :
#         return 1/base * power(base, n + 1)
#     elif n % 2 == 0:
#         a = power(base, n // 2)
#         return a * a
#     return  base * power(base, n - 1)

# print(power(2, -1))

# GREATEST COMMON DIVISOR

# def GCD(a, b):
#     assert int(a) == a and int(b) == b, "Number must be integer"
#     if a < 0:
#         a = -a
#     if b < 0:
#         b = -b
#     if b == 0:
#         return a
#     else:
#         return GCD(b, a%b)
    
# print(GCD(-8, 36))

# Decimal to Binary

def convert(n, k):
    assert int(n) == n, "Parameter must be integer"
    if n == 0:
        return 0
    else:
        return n % k + 10 * convert(int(n/k), k)
    
print(convert(5, 3))