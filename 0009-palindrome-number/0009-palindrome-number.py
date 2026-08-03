class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        result = 0
        while num > 0:
            temp = num % 10
            result = result * 10 + temp
            num = num // 10
        
        return result == x
        