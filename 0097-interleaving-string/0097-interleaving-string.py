class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)

        # dp[i][j] = whether s3[:i+j] can be formed
        # using s1[:i] and s2[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):

                if i > 0:
                    # Take the next character from s1
                    if dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]:
                        dp[i][j] = True

                if j > 0:
                    # Take the next character from s2
                    if dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]:
                        dp[i][j] = True

        return dp[m][n]
