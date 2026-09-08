class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                # mid is bad, so the first bad version is
                # mid or somewhere before it.
                right = mid
            else:
                # mid is good, so first bad version must be after mid.
                left = mid + 1

        return left
