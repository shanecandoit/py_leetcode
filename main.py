
""" 73. Set Matrix Zeroes
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

"""

from typing import List

class Solution:
    def setZeroes(self, matrix):
        """
        Do not rotate the matrix - modify it in place with O(1) extra memory.
        """
        if not matrix or not matrix[0]:
            return
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Check if first row contains any zero
        first_row_has_zero = any(cell == 0 for cell in matrix[0])
        
        # Check if first column contains any zero
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))
        
        # Mark zeros in other rows/columns
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set zeros based on marked rows and columns
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0
        
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0
        
        # Handle first row
        if first_row_has_zero:
            for j in range(cols):
                matrix[0][j] = 0
        
        # Handle first column
        if first_col_has_zero:
            for i in range(rows):
                matrix[i][0] = 0

# ex1
matrix = [[1,1,1],[1,0,1],[1,1,1]]
Solution().setZeroes(matrix)
want = [[1,0,1],[0,0,0],[1,0,1]]
print(matrix == want, matrix, want)

# ex2
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Solution().setZeroes(matrix)
want = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
print(matrix == want, matrix, want)

# True [[1, 0, 1], [0, 0, 0], [1, 0, 1]] [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
# True [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]] [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

# https://leetcode.com/problems/set-matrix-zeroes/?envType=daily-question&envId=2025-05-21
# Runtime 3 ms
# Beats 73.13%
# Memory 18.38 MB
# Beats 78.46%
