class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
           
        num = abs(x)
        result = 0
        while num > 0:
            temp = num % 10
            result = (result * 10) + temp
            num = num // 10
        if not (-2**31 <= result <= 2**31 - 1):
            return 0
        if x > 0 :
            return result
        else:
            return -result
        