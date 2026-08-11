class Solution:
    def print_fact(self, n):
        if n ==0:
             
            return 1

        return n * self.print_fact(n-1)   # Go till the end

obj = Solution()
print(obj.print_fact(5))