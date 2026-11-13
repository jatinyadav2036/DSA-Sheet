
class Solution(object):
    def largeGroupPositions(self, s):
        res = []
        i = 0

        while i < len(s):
            start = i

            while i < len(s) and s[i] == s[start]:
                i += 1

            if i - start >= 3:
                res.append([start, i - 1])

        return res
