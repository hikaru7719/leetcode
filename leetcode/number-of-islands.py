from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    self.helper(grid, i, j)
                    count += 1
        return count

    def helper(self, grid: List[List[str]], i: int, j: int):
        queue = deque([(i, j)])
        while queue:
            ii, jj = queue.pop()
            for i, j in [(ii + 1, jj), (ii - 1, jj), (ii, jj + 1), (ii, jj - 1)]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                    grid[i][j] = "0"
                    queue.append((i, j))
