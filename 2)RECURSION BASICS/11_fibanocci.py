class Solution(object):
    def fibonacci(self, n):
        f = [0] * n

        if n >= 1:
            f[0] = 0
        if n >= 2:
            f[1] = 1

        for i in range(2, n):
            f[i] = f[i - 1] + f[i - 2]

        return f


obj = Solution()
print(obj.fibonacci(7))


#using multiple recursion
class Solution(object):
    def fibonacci(self, n):
        if n<=1:
            return n
        return self.fibonacci(n-1)+self.fibonacci(n-2)
obj = Solution()
print(obj.fibonacci(7))