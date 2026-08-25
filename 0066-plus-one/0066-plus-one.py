class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Traverse the list from the last element to the first
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            
        # If the loop finishes, it means all digits were 9 (e.g., [9, 9, 9])
        # We need to create a new list with 1 followed by the zeros
        return [1] + digits
