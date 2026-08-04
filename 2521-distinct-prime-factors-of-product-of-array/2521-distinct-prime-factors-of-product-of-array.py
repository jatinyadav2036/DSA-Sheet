class Solution(object):
    def distinctPrimeFactors(self, nums):
        n = max(nums)
        s = set()
        primes = [x for x in range(2,n+1) if all(x % i != 0 for i in range(2,int(x**0.5) + 1))]

        for i in primes:
            for j in nums:
                if j % i == 0:
                    s.add(i)
        return len(s)

            
        