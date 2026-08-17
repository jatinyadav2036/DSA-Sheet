class Solution(object):
    def fib(self, n):
        def fb(num):
            if num == 0 or num == 1:
                return num
            return fb(num-1) + fb(num-2)
        return fb(n)
        