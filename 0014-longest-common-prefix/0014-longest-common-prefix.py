class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
            
        # Sort the array lexicographically
        strs.sort()
        
        # Compare the first and last string after sorting
        first = strs[0]
        last = strs[-1]
        ans = []
        
        # Find the common characters between first and last
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            ans.append(first[i])
            
        return "".join(ans)
