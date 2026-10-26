class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        dp0, dp1 = 0, 0

        for i in range(2, n + 1):
            curr = min(dp1 + cost[i - 1], dp0 + cost[i - 2])
            dp0, dp1 = dp1, curr

        return dp1
