class Solution:
    def countGoodNumbers(self, n: int) -> int:
        M = 10**9+7

        def power(base,exp):
            if exp == 0 :
                return 1
            elif exp % 2 == 0:
                ans = power(base,exp//2)
                return (ans*ans)%M
            
            else:
                return (base * power(base, exp - 1)) % M

        
        even_places = (n+1)//2
        odd_places = n // 2


        return (power(5,even_places)*power(4,odd_places))%M