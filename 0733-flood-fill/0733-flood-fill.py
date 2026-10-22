class Solution(object):
    def floodFill(self, image, sr, sc, color):
        original = image[sr][sc]

        # If the pixel already has the target color, do nothing
        if original == color:
            return image

        m, n = len(image), len(image[0])

        def dfs(r, c):
            # Check boundaries and original color
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if image[r][c] != original:
                return

            # Change the pixel color
            image[r][c] = color

            # Visit all four adjacent pixels
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)
        return image