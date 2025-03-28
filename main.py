from typing import List
import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        k = len(queries)

        sorted_queries = sorted([(query, i) for i, query in enumerate(queries)])
        result = [0] * k

        heap = [(grid[0][0], 0, 0)]
        visited = set()
        points = 0
        dp = {}

        query_index = 0
        while query_index < k:
            query, index = sorted_queries[query_index]

            while heap and heap[0][0] < query:
                val, i, j = heapq.heappop(heap)
                if (i, j) in visited:
                    continue
                visited.add((i, j))
                points += 1
                dp[(i, j)] = query

                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_i, new_j = i + di, j + dj
                    if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in visited:
                        heapq.heappush(heap, (grid[new_i][new_j], new_i, new_j))

            result[index] = points
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
