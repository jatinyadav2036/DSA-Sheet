class Solution(object):
    def selfDividingNumbers(self, left, right):
        result = []

        for num in range(left, right + 1):
            n = num
            is_self_dividing = True

            while n > 0:
                digit = n % 10

                # A number cannot contain zero,
                # and it must be divisible by every digit.
                if digit == 0 or num % digit != 0:
                    is_self_dividing = False
                    break

                n //= 10

            if is_self_dividing:
                result.append(num)

        return result