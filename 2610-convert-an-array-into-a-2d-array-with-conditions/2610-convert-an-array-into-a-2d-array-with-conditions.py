class Solution(object):
    def findMatrix(self, nums):
        hsh = dict()
        for i in nums:
            hsh[i] = hsh.get(i,0) + 1
        arr = []
        mx = max(hsh.values())
        for j in range(mx):
            arr.append([])
        for k in hsh:
            for l in range(hsh[k]):
                arr[l].append(k)
        return arr
        
        