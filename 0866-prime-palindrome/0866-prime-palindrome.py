class Solution(object):
    def primePalindrome(self, n):
        if n <= 2:
            return 2

        def is_prime(num):
            if num < 2: 
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True

        if 8 <= n <= 11:
            return 11
        
        temp = n
        while True:
            if 10**1 < temp < 10**2 :
                temp = 10 ** 2
            elif 10**3 < temp < 10**4 :
                temp = 10 ** 4
            elif 10**5 < temp < 10**6 :
                temp = 10 ** 6
            elif 10**7 < temp < 10**8 :
                temp = 10 ** 8

            s = str(temp)
            if s == s[::-1]:
                if is_prime(temp):
                    return temp

            if temp % 2 == 0:
                temp +=1 
            else:
                temp += 2            


        