# What is Dynamic Programming?

# Dynamic Programming is an algorithmic technique for solving an optimization problem by breaking it down into simpler sub-problems and utilizing the fact that the optimal solution to the overall problem depends on upon the optimal solution.

# Say we want to find the sum of an array. 1+1=2
# and 1+1+2=4. We remember the solution of 1+1 and then solve the problem making it efficient.

# 2 Main properties:
# Optimal Substructure required: If any problems overall optimal solution  can be constructed from the optimal solutions of its subproblem then this problem has optimal substructure.

# Eg: Fib(n) = Fib(n-1) + Fib(n-2)

# Overlapping Subproblems

# Subproblems are smaller versions of the original solution. Any problem  has overlapping subproblems if finding its solution involved the same subproblem multiple times.

# Not related to changing solutions etc. 

# Top Down with Memorization

# Solve the bigger problem by recursively finding the solution to smaller subproblems. Whenever wee solve a subproblem we cache its results so we don't have to repeatedly solve the same subproblem. If its called multiple times. This technique stores the results of already solved subproblems is called memorization.

# If we call a function recursively then it has exponential time complexity O(c^n). 

# Fibonacci Problem using Dynamic Programming

class Fib():
    def __init__(self):
        self.memo = {}
        
    def solveFib(self, n):
        if n == 1:
            return 0
        if n == 2:
            return 1
        if n not in self.memo:
            self.memo[n] = self.solveFib(n-1) + self.solveFib(n-2)
        return self.memo[n]
fib = Fib()
print(fib.solveFib(7))

# Bottom Up approach using tabulation

# Tabulation is the opposite of top down approach and avoids recursion. In this approach, we solve the problem "bottom-up" by solving the smaller sub-problems first. This is done by filling up a table, based on the results of the table the solution to the top/original problem is computed.

def fibonacciTab(n):
    tb = [0,1]
    # Iterate thru 2 to n+1 and then keep appending to list.
    for i in range(2, n+1):
        tb.append(tb[i-1]+tb[i-2])
    return tb[n-1]

print(fibonacciTab(7))

# Top Down Approach vs Bottom Up Approach

# top dwn is easy to come up with sol in comparison to bottom up.
# Runtime for TD is slow but bottom up is fast
# In terms of Space efficiency, unnecessary use of stack in TD but stack is not used in bottom up.
# Use TD for quick sol but BU apprach for efficient solution. 

# Is merge sort dynamic programming?

# Merge sort is not dynamic programming because although it may have optimal solution, it oes not have overlapping property. Not a single subproblem is repeated. We can solve it with simply divide and conquer algorithm.