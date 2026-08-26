class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        # Loop from the back of both strings until both are exhausted and no carry remains
        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
                
            # The current binary digit is the remainder of total divided by 2
            result.append(str(total % 2))
            # The carry is the quotient of total divided by 2
            carry = total // 2
            
        # Reverse the result list since we added digits from right to left
        return "".join(result[::-1])
