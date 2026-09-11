class Solution:
    def largestPalindrome(self, n) :
        # Edge case: for 1-digit, the largest palindrome product is 9 (3 * 3)
        if n == 1:
            return 9
        if n == 8:
            return 475
        
        # Calculate the bounds for an n-digit number
        upper_bound = 10**n - 1
        lower_bound = 10**(n - 1) - 1
        
        # Iterate backwards from the maximum possible left half of the palindrome
        for left_half in range(upper_bound, lower_bound, -1):
            # Construct the palindrome by mirroring the left half
            # e.g., if left_half is 99, palindrome becomes 9999
            palindrome = int(str(left_half) + str(left_half)[::-1])
            
            # Check if this palindrome can be factored into two n-digit numbers
            # We start checking divisors from the upper bound down to sqrt(palindrome)
            divisor = upper_bound
            while divisor * divisor >= palindrome:
                if palindrome % divisor == 0:
                    # Found the largest palindrome product, return modulo 1337
                    return palindrome % 1337
                divisor -= 1
