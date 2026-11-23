
class Solution(object):
    def surfaceArea(self, grid):
        n = len(grid)
        area = 0

        for i in range(n):
            for j in range(n):
                h = grid[i][j]

                if h == 0:
                    continue

                # Top and bottom faces
                area += 2

                # Four side faces
                area += 4 * h

                # Overlap with upper neighbor
                if i > 0:
                    area -= 2 * min(h, grid[i-1][j])

                # Overlap with left neighbor
                if j > 0:
                    area -= 2 * min(h, grid[i][j-1])

        return area
