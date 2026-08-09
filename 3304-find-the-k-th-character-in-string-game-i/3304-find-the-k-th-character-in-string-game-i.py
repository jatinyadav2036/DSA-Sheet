class Solution(object):
    def kthCharacter(self, k):
        """
        :type k: int
        :rtype: str
        """
        # Calculate the 0-indexed position
        target_index = k - 1
        
        # Count the number of set bits (1s) in the binary representation
        set_bits = bin(target_index).count('1')
        
        # Shift the character 'a' by the number of set bits
        return chr(ord('a') + set_bits)
