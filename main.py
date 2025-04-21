""" 2145. Count the Hidden Sequences

You are given a 0-indexed array of n integers differences, 
which describes the differences between each pair of consecutive integers of a hidden sequence of length (n + 1). 
More formally, call the hidden sequence hidden, then we have that differences[i] = hidden[i + 1] - hidden[i].

You are further given two integers lower and upper that describe the inclusive range of values [lower, upper] 
that the hidden sequence can contain.

For example, given differences = [1, -3, 4], lower = 1, upper = 6, 
the hidden sequence is a sequence of length 4 whose elements are in between 1 and 6 (inclusive).
[3, 4, 1, 5] and [4, 5, 2, 6] are possible hidden sequences.
[5, 6, 3, 7] is not possible since it contains an element greater than 6.
[1, 2, 3, 4] is not possible since the differences are not correct.
Return the number of possible hidden sequences there are. If there are no possible sequences, return 0.

Example 1:
    Input: differences = [1,-3,4], lower = 1, upper = 6
    Output: 2
    Explanation: The possible hidden sequences are:
    - [3, 4, 1, 5]
    - [4, 5, 2, 6]
    Thus, we return 2.

Example 2:
    Input: differences = [3,-4,5,1,-2], lower = -4, upper = 5
    Output: 4
    Explanation: The possible hidden sequences are:
    - [-3, 0, -4, 1, 2, 0]
    - [-2, 1, -3, 2, 3, 1]
    - [-1, 2, -2, 3, 4, 2]
    - [0, 3, -1, 4, 5, 3]
    Thus, we return 4.

Example 3:
    Input: differences = [4,-7,2], lower = 3, upper = 6
    Output: 0
    Explanation: There are no possible hidden sequences. Thus, we return 0.
"""

from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        n = len(differences)
        min_val = 0
        max_val = 0
        curr_val = 0
        for diff in differences:
            curr_val += diff
            min_val = min(min_val, curr_val)
            max_val = max(max_val, curr_val)
        # The range of the first element is [lower - min_val, upper - max_val]
        # The number of valid first elements is the size of this range  
        # The size of the range is (upper - max_val) - (lower - min_val) + 1

        return max(0, (upper - max_val) - (lower - min_val) + 1)

# ex 1
differences = [1,-3,4]
lower = 1
upper = 6
got = Solution().numberOfArrays(differences, lower, upper)
want = 2
print(got == want, got, want)

# ex 2
differences = [3,-4,5,1,-2]
lower = -4
upper = 5
got = Solution().numberOfArrays(differences, lower, upper)
want = 4
print(got == want, got, want)

# ex 3
differences = [4,-7,2]
lower = 3
upper = 6
got = Solution().numberOfArrays(differences, lower, upper)
want = 0
print(got == want, got, want)

# https://leetcode.com/problems/count-the-hidden-sequences/submissions/1613769669/?envType=daily-question&envId=2025-04-21
# Runtime 155 ms
# Beats 43.43%
# Memory 32.28 MB
# Beats 75.76%
