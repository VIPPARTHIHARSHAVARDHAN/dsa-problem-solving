class Solution(object):
    def removeOuterParentheses(self, s):
        result = ""
        count = 0

        for ch in s:
            if ch == "(":
                count += 1

                if count > 1:
                    result += ch

            else:
                count -= 1

                if count > 0:
                    result += ch

        return result


# Object creation
obj = Solution()

# Input
s = "(()())(())"

# Function call
answer = obj.removeOuterParentheses(s)

# Output
print(answer)