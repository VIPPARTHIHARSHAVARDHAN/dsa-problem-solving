class Solution(object):
    def myAtoi(self, s):

        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1

        elif i < n and s[i] == '+':
            i += 1

        result = 0

        while i < n:

            integer = ord(s[i]) - ord('0')

            if integer < 0 or integer > 9:
                break

            result = result * 10 + integer
            i += 1

        result = result * sign

        if result < -2**31:
            return -2**31

        if result > 2**31 - 1:
            return 2**31 - 1

        return result