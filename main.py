
""" 2962. Count Subarrays Where Max Element Appears at Least K Times
You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.

Example 1:
    Input: nums = [1,3,2,3,3], k = 2
    Output: 6
    Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

Example 2:
    Input: nums = [1,4,2,1], k = 3
    Output: 0
    Explanation: No subarray contains the element 4 at least 3 times.
"""

from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_num = max(nums)
        count = 0
        left = 0
        max_count = 0

        for right in range(n):
            if nums[right] == max_num:
                max_count += 1

            while max_count >= k:
                if nums[left] == max_num:
                    max_count -= 1
                left += 1
            count += left

        return count

# ex 1
nums = [1,3,2,3,3]
k = 2
got = Solution().countSubarrays(nums, k)
want = 6
print(f'got={got}, want={want}, ok={got==want}')

# ex 2
nums = [1,4,2,1]
k = 3
got = Solution().countSubarrays(nums, k)
want = 0
print(f'got={got}, want={want}, ok={got==want}')

# ex 3
nums = [61,23,38,23,56,40,82,56,82,82,82,70,8,69,8,7,19,14,58,42,82,10,82,78,15,82]
k = 2
got = Solution().countSubarrays(nums, k)
want = 224
print(f'got={got}, want={want}, ok={got==want}')

# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/submissions/1621238576/?envType=daily-question&envId=2025-04-29
# Runtime 74 ms
# Beats 74.92%
# Memory 29.66 MB
# Beats 37.54%
