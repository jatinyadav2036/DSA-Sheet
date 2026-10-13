class Solution(object):
    def findShortestSubArray(self, nums):
        count = {}
        first = {}
        degree = 0
        min_length = len(nums)

        for i, num in enumerate(nums):
            if num not in count:
                count[num] = 0
                first[num] = i

            count[num] += 1

            if count[num] > degree:
                degree = count[num]
                min_length = i - first[num] + 1
            elif count[num] == degree:
                min_length = min(min_length, i - first[num] + 1)

        return min_length