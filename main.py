
""" 2302. Count Subarrays With Score Less Than K
The score of an array is defined as the product of its sum and its length.

For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.

A subarray is a contiguous sequence of elements within an array.

Example 1:
    Input: nums = [2,1,4,3,5], k = 10
    Output: 6
    Explanation:
    The 6 subarrays having scores less than 10 are:
    - [2] with score 2 * 1 = 2.
    - [1] with score 1 * 1 = 1.
    - [4] with score 4 * 1 = 4.
    - [3] with score 3 * 1 = 3. 
    - [5] with score 5 * 1 = 5.
    - [2,1] with score (2 + 1) * 2 = 6.
    Note that subarrays such as [1,4] and [4,3,5] are not considered because their scores are 10 and 36 respectively, while we need scores strictly less than 10.

Example 2:
    Input: nums = [1,1,1], k = 5
    Output: 5
    Explanation:
    Every subarray except [1,1,1] has a score less than 5.
    [1,1,1] has a score (1 + 1 + 1) * 3 = 9, which is greater than 5.
    Thus, there are 5 subarrays having scores less than 5.
"""

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        l = 0
        s = 0
        for r in range(n):
            s += nums[r]
            while s * (r - l + 1) >= k:
                s -= nums[l]
                l += 1
            ans += r - l + 1
        return ans

# ex 1
nums = [2,1,4,3,5]
k = 10
result = Solution().countSubarrays(nums, k)
want = 6
print(f"want: {want}, result: {result}, test: {result == want}")
# ex 2
nums = [1,1,1]
k = 5
result = Solution().countSubarrays(nums, k)
want = 5
print(f"want: {want}, result: {result}, test: {result == want}")

# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/submissions/1620493200/?envType=daily-question&envId=2025-04-28
# Runtime 111 ms
# Beats 85.60%
# Memory 30.41 MB
# Beats 61.29%
