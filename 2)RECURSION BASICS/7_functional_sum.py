class Solution:
    def print_fsum(self, n):
        if n ==0:
             
            return 0

        return n + self.print_fsum(n-1)   # Go till the end

obj = Solution()
print(obj.print_fsum(5))