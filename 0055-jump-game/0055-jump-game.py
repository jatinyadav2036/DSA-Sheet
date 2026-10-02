class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest = 0

        for i in range(len(nums)):
            # If we can't even reach this index, we're stuck.
            if i > farthest:
                return False

            # Update the farthest position we can reach.
            farthest = max(farthest, i + nums[i])

            # We can already reach the last index.
            if farthest >= len(nums) - 1:
                return True

        return True
