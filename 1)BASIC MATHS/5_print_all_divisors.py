class Solution(object):
    def divisors(self, n):
        for i in range(1, n + 1):
            if n % i == 0:
                print(i,end=" ")

obj = Solution()
obj.divisors(12)