class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, self.dfs(grid, i, j))
        return res

    def dfs(self, grid, i, j):
        if(i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1):
            return 0
        grid[i][j] = -1
        return 1 + self.dfs(grid, i + 1, j) + self.dfs(grid, i - 1, j) + self.dfs(grid, i, j + 1) + self.dfs(grid, i, j - 1)