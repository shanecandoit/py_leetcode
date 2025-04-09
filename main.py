
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
        """
        Calculates the minimum number of operations to make array values equal to k.

        Args:
            nums: The input list of integers.
            k: The target value.

        Returns:
            The minimum operations, or -1 if it's impossible.
        """

        if any(num < k for num in nums):
            return -1

        unique_greater_than_k = set()
        for num in nums:
            if num > k:
                unique_greater_than_k.add(num)

        if not unique_greater_than_k:
            return 0  # Handle the case where no elements are greater than k.

        return len(unique_greater_than_k)  # The length of the set is the minimum operations


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

# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/submissions/1601841960/?envType=daily-question&envId=2025-04-09
# Runtime 73 ms
# Beats 18.63%
# Memory 17.62 MB
# Beats 75.47%
