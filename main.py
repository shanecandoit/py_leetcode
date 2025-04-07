
"""
416. Partition Equal Subset Sum
Given an integer array nums, return true if you can partition the array into two subsets 
such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:
    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
    Input: nums = [1,2,3,5]
    Output: false
    Explanation: The array cannot be partitioned into equal sum subsets.
"""

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # If the total sum is odd, we cannot partition it into two equal subsets
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        
        # dp set will store all possible sums achievable using subsets of nums
        dp = {0}

        for num in nums:
            # Create a temporary set to store new sums for this iteration
            # to avoid modifying dp while iterating over it.
            next_dp_adds = set()
            for current_sum in dp:
                new_sum = current_sum + num
                if new_sum == target:
                    return True
                # Only add sums less than target to keep the set size manageable
                if new_sum < target:
                    next_dp_adds.add(new_sum)
            
            # Update dp with the newly found sums
            dp.update(next_dp_adds)
            
            # Optimization: if a number itself is the target (and hasn't been found yet)
            # This case is implicitly handled when current_sum is 0, but explicit check might be slightly faster
            # if num == target:
            #     return True
            # Note: The check `if num > target: continue` is generally useful but removed here
            # as the core logic handles it by not adding sums > target.

        # If the loop finishes without finding the target sum
        return False
    
if __name__ == "__main__":
    
    # ex 1
    nums = [1,5,11,5]
    result = Solution().canPartition(nums)
    want = True
    print( result == want, want, result)

    # ex 2
    nums = [1,2,3,5]
    result = Solution().canPartition(nums)
    want = False
    print( result == want, want, result)

# https://leetcode.com/problems/partition-equal-subset-sum/submissions/1599668054/?envType=daily-question&envId=2025-04-07
# Runtime 190 ms
# Beats 94.65%
# Memory 19.42 MB
# Beats 56.59%
