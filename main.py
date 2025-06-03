
""" 1298. Maximum Candies You Can Get from Boxes
You have n boxes labeled from 0 to n - 1.
You are given four arrays: status, candies, keys, and containedBoxes where:

- status[i] is 1 if the ith box is open and 0 if the ith box is closed,
- candies[i] is the number of candies in the ith box,
- keys[i] is a list of the labels of the boxes you can open after opening the ith box.
- containedBoxes[i] is a list of the boxes you found inside the ith box.

You are given an integer array initialBoxes that contains the labels of the boxes you initially have.
You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.

Return the maximum number of candies you can get following the rules above.

Example 1:
    Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
    Output: 16
    Explanation: You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2.
    Box 1 is closed and you do not have a key for it so you will open box 2. You will find 4 candies and a key to box 1 in box 2.
    In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed.
    Total number of candies collected = 7 + 4 + 5 = 16 candy.

Example 2:
    Input: status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]
    Output: 6
    Explanation: You have initially box 0. Opening it you can find boxes 1,2,3,4 and 5 and their keys.
    The total number of candies will be 6.
"""

import collections
from typing import List

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]],
                   containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        max_candies = 0
        open_boxes = set()
        # Use collections.deque for efficient pop(0)
        closed_boxes_queue = collections.deque(initialBoxes)
        
        # Keep track of boxes we've encountered but couldn't open yet
        found_but_closed = set()

        # Keep track of keys we have
        current_keys = set(i for i, s in enumerate(status) if s == 1)

        while closed_boxes_queue:
            box_idx = closed_boxes_queue.popleft()

            # If we have the key for this box and haven't opened it yet
            if box_idx in current_keys and box_idx not in open_boxes:
                max_candies += candies[box_idx]
                open_boxes.add(box_idx)

                # Add new keys found in this box
                for key in keys[box_idx]:
                    current_keys.add(key)
                    # If we now have the key for a box we found earlier but couldn't open
                    if key in found_but_closed:
                        closed_boxes_queue.append(key)
                        found_but_closed.remove(key)

                # Add new boxes found inside this box
                for contained in containedBoxes[box_idx]:
                    if contained not in open_boxes: # Avoid re-processing already open boxes
                        if contained in current_keys:
                            closed_boxes_queue.append(contained)
                        else:
                            found_but_closed.add(contained)
            elif box_idx not in open_boxes: # If we don't have the key yet, mark as found but closed
                 found_but_closed.add(box_idx)


        return max_candies

# ex1
status = [1, 0, 1, 0]
candies = [7, 5, 4, 100]
keys = [[], [], [1], []]
containedBoxes = [[1, 2], [3], [], []]
initialBoxes = [0]
want = 16
got = Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes)
print(got == want, f"Expected {want}, but got {got}")

# ex2
status = [1, 0, 0, 0, 0, 0]
candies = [1, 1, 1, 1, 1, 1]
keys = [[1, 2, 3, 4, 5], [], [], [], [], []]
containedBoxes = [[1, 2, 3, 4, 5], [], [], [], [], []]
initialBoxes = [0]
want = 6
got = Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes)
print(got == want, f"Expected {want}, but got {got}")


# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/submissions/1652936505/?envType=daily-question&envId=2025-06-03
# Runtime 30 ms
# Beats 30.65%
# Memory 28.02 MB
# Beats 86.97%
