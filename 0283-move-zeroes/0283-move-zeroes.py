class Solution(object):
    def moveZeroes(self, nums):
        if len(nums) < 2:
            return nums
        left = 0 
        right = 0
        while right != len(nums):
            if nums[left] == 0 and nums[right] != 0 :
                nums[left] , nums[right] = nums[right] , nums[left]
            if nums[left] != 0 :
                left += 1
            right += 1
                
        return nums
        