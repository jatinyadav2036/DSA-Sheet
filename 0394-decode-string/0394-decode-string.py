class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curr = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                # Save the current string and repeat count
                stack.append((curr, num))
                curr = ""
                num = 0

            elif ch == ']':
                # Get the string and count before this bracket
                prev, repeat = stack.pop()
                curr = prev + curr * repeat

            else:
                curr += ch

        return curr