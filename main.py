
""" 1346. Check If N and Its Double Exist
Given an array arr of integers, check if there exist two indices i and j such that :
    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]
 
Example 1:
    Input: arr = [10,2,5,3]
    Output: true
    Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
    Input: arr = [3,1,7,11]
    Output: false
    Explanation: There is no i and j that satisfy the conditions.
"""

from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        # can we O(n) ?
        # Store all numbers in a set for O(1) lookup
        seen = set()
        
        for num in arr:
            # Do not iterate through twice
            # Check if either double or half exists
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            # Add current number to seen set
            seen.add(num)
        
        return False


# ex 1
arr = [10,2,5,3]
result = Solution().checkIfExist(arr)
want = True
print(f"ex1 want: {want}, result: {result}, test: {result == want}")

# ex 2
arr = [3,1,7,11]
result = Solution().checkIfExist(arr)
want = False
print(f"ex2 want: {want}, result: {result}, test: {result == want}")

# ex 3
arr = [-2,0,10,-19,4,6,-8]
result = Solution().checkIfExist(arr)
want = False
print(f"ex3 want: {want}, result: {result}, test: {result == want}")

# ex 4
arr = [0, 0]
result = Solution().checkIfExist(arr)
want = True
print(f"ex4 want: {want}, result: {result}, test: {result == want}")

'''
ex1 want: True, result: True, test: True
ex2 want: False, result: False, test: True
ex3 want: False, result: False, test: True
ex4 want: True, result: True, test: True
'''

# https://leetcode.com/problems/check-if-n-and-its-double-exist/submissions/1621211492/?envType=daily-question&envId=2025-04-29
# Runtime 0 ms
# Beats 100.00%
# Memory 17.77 MB
# Beats 80.04%
