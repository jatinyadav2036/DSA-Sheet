
class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)

        diff = (aliceSum - bobSum) // 2

        bobSet = set(bobSizes)

        for a in aliceSizes:
            b = a - diff

            if b in bobSet:
                return [a, b]
