
""" 2094. Finding 3-Digit Even Numbers
You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.

Example 1:
    Input: digits = [2,1,3,0]
    Output: [102,120,130,132,210,230,302,310,312,320]
    Explanation: All the possible integers that follow the requirements are in the output array. 
    Notice that there are no odd integers or integers with leading zeros.

Example 2:
    Input: digits = [2,2,8,8,2]
    Output: [222,228,282,288,822,828,882]
    Explanation: The same digit can be used as many times as it appears in digits. 
    In this example, the digit 8 is used twice each time in 288, 828, and 882. 

Example 3:
    Input: digits = [3,7,5]
    Output: []
    Explanation: No even integers can be formed using the given digits.
"""

from typing import List
import collections

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # Count the frequency of each digit in the input
        digit_counts = collections.Counter(digits)
        result = []

        # Iterate through all possible 3-digit even numbers
        for num in range(100, 1000, 2):
            # Extract digits of the current number
            d1 = num // 100
            d2 = (num // 10) % 10
            d3 = num % 10

            # Count the frequency of digits needed for the current number
            num_digit_counts = collections.Counter([d1, d2, d3])

            # Check if the digits required for 'num' are available in 'digits'
            is_possible = True
            for d, count in num_digit_counts.items():
                if digit_counts[d] < count:
                    is_possible = False
                    break

            if is_possible:
                result.append(num)

        # The numbers are generated in increasing order, so the list is already sorted.
        return result

# ex 1
digits = [2, 1, 3, 0]
got = Solution().findEvenNumbers(digits)
want = [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
print(got == want, got)  # Output: True [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]

# ex 2
digits = [2, 2, 8, 8, 2]
got = Solution().findEvenNumbers(digits)
want = [222, 228, 282, 288, 822, 828, 882]
print(got == want, got)  # Output: True [222, 228, 282, 288, 822, 828, 882]

# ex 3
digits = [3, 7, 5]
got = Solution().findEvenNumbers(digits)
want = []
print(got == want, got)  # Output: True []

# https://leetcode.com/problems/finding-3-digit-even-numbers/submissions/1632082424/?envType=daily-question&envId=2025-05-12
# Runtime 39 ms
# Beats 72.51%
# Memory 18.10 MB
# Beats 12.99%
