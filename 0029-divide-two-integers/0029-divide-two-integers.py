class Solution(object):
    def divide(self, dividend, divisor):
        # 32-bit signed integer limits
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        # Handle overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine final sign
        is_negative = (dividend < 0) ^ (divisor < 0)

        # Work with absolute values
        a = abs(dividend)
        b = abs(divisor)
        cnt = 0

        # Iterate downwards from the largest possible 32-bit shift
        for i in range(31, -1, -1):
            # Check if b * (2^i) fits inside a
            if (b << i) <= a:
                a -= (b << i)      # Subtract the matched block
                cnt += (1 << i)    # Add the power of 2 to the quotient

        return -cnt if is_negative else cnt
