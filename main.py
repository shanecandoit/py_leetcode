
""" 3375. Minimum Operations to Make Array Values Equal to K
You are given an integer array nums and an integer k.

An integer h is called valid if all values in the array that are 
strictly greater than h are identical.

For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 
because all nums[i] > 9 are equal to 10, but 5 is not a valid integer.

You are allowed to perform the following operation on nums:

Select an integer h that is valid for the current values in nums.
For each index i where nums[i] > h, set nums[i] to h.
Return the minimum number of operations required 
to make every element in nums equal to k. If it is impossible 
to make all elements equal to k, return -1.

Example 1:
    Input: nums = [5,2,5,4,5], k = 2
    Output: 2
    Explanation:
    The operations can be performed in order using valid integers 4 and then 2.

Example 2:
    Input: nums = [2,1,2], k = 2
    Output: -1
    Explanation:
    It is impossible to make all the values equal to 2.

Example 3:
    Input: nums = [9,7,5,3], k = 1
    Output: 4
    Explanation:
    The operations can be performed using valid integers in the order 7, 5, 3, and 1.
"""
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # 1. Check if any element is less than k
        if any(num < k for num in nums):
            return -1

        # 2. Count unique elements strictly greater than k
        # Use a set for efficient counting of unique elements
        unique_greater_than_k = set()
        for num in nums:
            if num > k:
                unique_greater_than_k.add(num)

        # 3. The number of operations is the count of these unique elements
        return len(unique_greater_than_k)


if __name__ == "__main__":

    # ex 1
    nums = [5,2,5,4,5]
    k = 2
    got = Solution().minOperations(nums, k)
    want = 2
    print(f"got: {got}, want: {want}, correct: {got == want}")

    # ex 2
    nums = [2,1,2]
    k = 2
    got = Solution().minOperations(nums, k)
    want = -1
    print(f"got: {got}, want: {want}, correct: {got == want}")

    # ex 3
    nums = [9,7,5,3]
    k = 1
    got = Solution().minOperations(nums, k)
    want = 4
    print(f"got: {got}, want: {want}, correct: {got == want}")

# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/submissions/1601836852/?envType=daily-question&envId=2025-04-09
# Runtime 78 ms
# Beats 6.84%
# Memory 17.92 MB
# Beats 9.43%
