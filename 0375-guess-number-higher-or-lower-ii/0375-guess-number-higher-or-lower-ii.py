class Solution(object):
    def getMoneyAmount(self, n):
        # dp[i][j] represents the minimum cost to guarantee a win for the range [i, j]
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Length of the range
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                dp[i][j] = float('inf')
                
                # Try every number 'k' as the first guess in range [i, j]
                for k in range(i, j):
                    # Cost is k plus the max of the worst-case scenario from left or right subproblem
                    cost = k + max(dp[i][k - 1], dp[k + 1][j])
                    dp[i][j] = min(dp[i][j], cost)
                    
        return dp[1][n]
