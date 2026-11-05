
class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        ans = [float('inf')] * n

        # Left to right traversal
        prev = float('-inf')
        for i in range(n):
            if s[i] == c:
                prev = i
            ans[i] = i - prev

        # Right to left traversal
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans
