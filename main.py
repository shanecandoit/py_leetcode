
""" 135. Candy
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
    Input: ratings = [1,0,2]
    Output: 5
    Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
    Input: ratings = [1,2,2]
    Output: 4
    Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
    The third child gets 1 candy because it satisfies the above two conditions.
"""

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0

        candies = [1] * n

        # Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)

# ex1
ratings = [1,0,2]
want = 5
got = Solution().candy(ratings)
print(f"ex1: want={want}, got={got}, {'OK' if want == got else 'WRONG'}")

# ex2
ratings = [1,2,2]
want = 4
got = Solution().candy(ratings)
print(f"ex2: want={want}, got={got}, {'OK' if want == got else 'WRONG'}")

# https://leetcode.com/problems/candy/submissions/1651707798/?envType=daily-question&envId=2025-06-02
# Runtime 18 ms
# Beats 45.29%
# Memory 19.87 MB
# Beats 68.66%
