class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        n = len(bits)

        while i < n - 1:
            if bits[i] == 1:
                i += 2  # 1 starts a two-bit character
            else:
                i += 1  # 0 is a one-bit character

        return i == n - 1