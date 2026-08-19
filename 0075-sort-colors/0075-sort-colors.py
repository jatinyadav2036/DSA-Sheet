class Solution(object):
    def sortColors(self, nums):
        cnt = [0,0,0]
        for i in nums:
            if i == 0 :
                cnt[0] += 1
            elif i == 1:
                cnt[1] += 1
            else:
                cnt[2] += 1
        j = 0
        k = 0
        while j < len(nums):
            if cnt[k] != 0:
                nums[j] = k
                cnt[k] -= 1
                j += 1
            else:
                k += 1
        return nums


        