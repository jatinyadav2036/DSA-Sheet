class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases
        if n <= 2:
            return n
        
        # Initialize the first two steps
        first = 1
        second = 2
        
        # Calculate the combinations iteratively
        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current
            
        return second
