class Solution(object):

    def print_name(self, i,n):
        if i>n:
            return
        print("Harsha")
        self.print_name(i + 1,n)

obj = Solution()
n=5
obj.print_name(1,n)