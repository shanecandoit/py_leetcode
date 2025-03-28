from typing import List
import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        """
        Finds the maximum number of points reachable from the top-left corner of the grid for each query.

        Args:
            grid (List[List[int]]): The grid of integers.
            queries (List[int]): The list of query values.

        Returns:
            List[int]: The list of maximum number of points for each query.
        """
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        # Number of queries  
        k = len(queries)  

        # Sort queries with their original indices to restore the original order later
        sorted_queries = sorted([(query, i) for i, query in enumerate(queries)])
        # Initialize the result list
        result = [0] * k  

        # Initialize the heap with the starting cell (0, 0)
        # (value, row, col)
        heap = [(grid[0][0], 0, 0)]  
        # Keep track of visited cells
        visited = set()  
        # Keep track of the number of reachable points
        points = 0  
        # memoize intermediate results
        dp = {} 

        query_index = 0
        while query_index < k:
            # Get the current query and its original index
            query, index = sorted_queries[query_index]  

            # Keep popping cells from the heap until the current cell's value is greater than or equal to the query value
            while heap and heap[0][0] < query:
                # Get the cell with the smallest value
                _val, i, j = heapq.heappop(heap)  
                # If the cell has already been visited, skip it
                if (i, j) in visited:  
                    continue
                # Mark the cell as visited
                visited.add((i, j))  
                # Increment the number of reachable points
                points += 1  
                dp[(i, j)] = query

                # Add the neighbors of the current cell to the heap
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    # Calculate the coordinates of the neighbor
                    new_i, new_j = i + di, j + dj  
                    # If the neighbor is within the grid and has not been visited, add it to the heap
                    if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in visited:
                        heapq.heappush(heap, (grid[new_i][new_j], new_i, new_j))

            # Store the number of reachable points for the current query
            result[index] = points  
            # Move to the next query
            query_index += 1  

        return result


if __name__ == '__main__':
    print('2503. Maximum Number of Points From Grid Queries')

    # ex 1
    grid = [[1,2,3],[2,5,7],[3,5,1]]
    queries = [5,6,2]
    result = Solution().maxPoints(grid, queries)
    want = [5,8,1]
    print(f'grid = {grid}, queries = {queries} => {result}')
    print(f'want: {want}, result==want: {result==want}')

    # ex 2
    grid = [[5,2,1],[1,1,2]]
    queries = [3]
    result = Solution().maxPoints(grid, queries)
    want = [0]
    print(f'grid = {grid}, queries = {queries} => {result}')
    print(f'want: {want}, result==want: {result==want}')

# https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/submissions/1589249850/?envType=daily-question&envId=2025-03-28
# Runtime 1193 ms
# Beats 11.76%
# Memory 59.47 MB
# Beats 5.23%
