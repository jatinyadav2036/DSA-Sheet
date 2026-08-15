class Solution(object):
    def reverseWords(self, s):
        a = list(" ".join(s.split()))
        a.append(" ")
        arr = []
        q = 0
        for i in range(len(a)):
            if a[i] == " ":
                arr[:0] = a[q:i+1]
                q = i+1
        arr.pop()
        c = "".join(arr)
        return c
        
s  = Solution()
print(s.reverseWords("the sky is blue"))