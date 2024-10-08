# Divide & Conquer

# Divide and conquer is an algorithm design paradigm which works by recursively breaking down a problem into sub problems of a similar type, until these have become simple enough to be solved directly. The solutions to the sub problems are then combined to give a solution to the original problem.

# For example we're tasked with developing a website We break down this into smaller tasks such as backend, front end and design. Then we further divide them into smaller problems until they can be solved individually.

# Divide and conquer problems need to have optimal substructure property. Which means if any problems optimal solution can be constructed from the optimal solutions of its subproblem then this problem has optimal substructure.

# Fib(n) = Fib(n-1) + Fib(n-2)

# Why we need it?
# It is very effective when the problem has optimal substructure property.

# Let's take a look at some common divide and conquer algorithms.
# Example is merge sort, quicksort etc.

# Fibonacci Series using Divide and Conquer Approach

# First two numbers are always 0 and 1. Series goes like 0, 1, 1, 2, 3, 5, 8, 13, and so on..

def fibonacci(n):
    if n < 1:
        return "Error"
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))

# Number Factor Problem
# Given N, find the number of ways to express N as a sum of 1, 3 and 4.

# Example 1
#  N = 4
# Number of ways = 4

def numberFactor(n):
    if n in [0, 1, 2]:
        return 1
    elif n == 3:
        return 2
    else:
        subP1 =  numberFactor(n-1)
        subP2 =  numberFactor(n-3)
        subP3 =  numberFactor(n-4)
        return subP1 + subP2 + subP3
print(numberFactor(6)) 