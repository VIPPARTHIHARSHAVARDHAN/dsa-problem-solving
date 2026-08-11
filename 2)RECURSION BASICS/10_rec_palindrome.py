class Solution:
    def is_palindrome(self, s, i):
        n = len(s)

        if i >= n // 2:
            return True

        if s[i] != s[n - i - 1]:
            return False

        return self.is_palindrome(s, i + 1)


obj = Solution()

s = "madam"
print(obj.is_palindrome(s, 0))


#l,r
class Solution:
    def isPalindrome(self, s, i):
        n = len(s)

        if i >= n // 2:
            return True

        if s[i] != s[n - i - 1]:
            return False

        return self.isPalindrome(s, i + 1)

obj = Solution()

s = "madam"
print(obj.isPalindrome(s, 0))


#leetcode 125
class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True