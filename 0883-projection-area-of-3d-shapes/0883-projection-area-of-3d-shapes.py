class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        ans = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    ans += 1  # Top projection

            ans += max(grid[i])  # Front projection
            ans += max(grid[j][i] for j in range(n))  # Side projection

        return ans