# Backtracking

# A Backtracking algorithm is a problem solving algorithm that uses a brute force approach for finding the desired output using recursion. It tries out all possible solutions and gives out best solution. We're not looking for optimal solution. 

# 3 Types of problems that can be solved with backtracking are decision problems where we're searching for a feasible solution, optimization problem, where we search for best solution, and then enumeration problem which we find all feasible solutions.

# We can represent all states using a space state tree by recursively exploring this tree and check for validity of solution. If valid we continue to explore deeper, if not then we eliminate the entire subtree.

# Backtracking checks whether the given node is a valid solution or not. Discard several invalid solutions with one iteration. Enumerate all subtree of the node to find the valid solution.

# Eg: 3! = 6
# We can represent it as 3 colors. the number of different color combinations as a representation of a state space tree can represent all the possible valid solutions for the factorial problem. But in backtracking we'll have constraints so, say if we say that red color cannot be in middle, then in that case all such subtrees will be considered invalid where the middle node is red. So for this case we've 4 valid solutions.

# Difference between backtracking and brute force. Brute force checks every single solution of the problem but in backtracking we at each and every step check if whether pursing this solution further will lead to a valid solution or not and then discard or validate the solution. 

# The N Queens Problem

# The queen can move diagonally, straight and sideways. 
# Say we've a NxN chessboard, in what positions can be place N queens so that they do not attack each other.

# This can be solved with Backtracking

# Let's place the queen in the first row, first column, and then explore this tree and see if our constraints are violated or not. If yes, discard solution, if not pursue further.

# Algorithm
# 1. Start in the leftmost column
# 2. If all queens are placed: return True
# 3. Try all rows in the current column.
#     By following for every tried row.
#         a. If the queen can be placed safely in this row then mark this [row, column] as part of the solution and recursively check if placing queen here leads to solution.
#         b. If placing the queen in [row, column] leads toa  solution then return True
#         c. If placing queen doesn't lead to a solution then unmark this [row, column] {Backtrack} and go to step {a} to try other rows.
# 4. If all rows have been tried and nothing works, return false to trigger backtracking

# Implementation

class NQueens:
    def __init__(self, n) -> None:
        self.n = n
        self.chess_tables = [[0 for _ in range(n)] for _ in range(n)]
        
    def printQueens(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.chess_tables[i][j] == 1:
                    print("Q", end="")
                else:
                    print("-", end="")
            print()
        print()
    
    def isPlaceSafe(self, row_index, col_index):
        # Check horizontally (only left of the current column)
        for i in range(col_index):
            if self.chess_tables[row_index][i] == 1:
                return False
        
        # Check top-left diagonal
        i, j = row_index, col_index
        while i >= 0 and j >= 0:
            if self.chess_tables[i][j] == 1:
                return False
            i -= 1
            j -= 1
        
        # Check bottom-left diagonal
        i, j = row_index, col_index
        while i < self.n and j >= 0:
            if self.chess_tables[i][j] == 1:
                return False
            i += 1
            j -= 1
        
        # If no conflicts, the position is safe
        return True
    
    def solve(self, col_index):
        if col_index == self.n:
            return True
        for row_index in range(self.n):
            if self.isPlaceSafe(row_index, col_index):
                self.chess_tables[row_index][col_index] = 1
                if self.solve(col_index + 1):
                    return True
                # Backtrack if placing the queen didn't work
                self.chess_tables[row_index][col_index] = 0
        return False
    
    def solveNqueens(self):
        if self.solve(0):
            self.printQueens()
        else:
            print("There is no solution for the problem")

# Example Usage:
queens = NQueens(3)
queens.solveNqueens()

    
