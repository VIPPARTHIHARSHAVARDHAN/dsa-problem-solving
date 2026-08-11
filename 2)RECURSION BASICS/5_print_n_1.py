class Solution(object):

    def print_name(self, i,n):
        if n<i:
            return
        print(n)
        self.print_name(i,n-1)

obj = Solution()
n=5
obj.print_name(1,n)



#using backtraching
class Solution:
    def print_n(self, i, n):
        if i > n:
            return

        self.print_n(i + 1, n)   # Go till the end
        print(i)                 # Print while coming back

obj = Solution()
obj.print_n(1, 5)