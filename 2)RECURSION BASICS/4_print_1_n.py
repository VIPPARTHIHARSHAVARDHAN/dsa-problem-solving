class Solution(object):

    def print_name(self, i,n):
        if i>n:
            return
        print(i)
        self.print_name(i + 1,n)

obj = Solution()
n=5
obj.print_name(1,n)


#using backtraching
class Solution(object):

    def print_name(self, i,n):
        if i<1:
            return
        
        self.print_name(i - 1,n)
        print(i)

obj = Solution()
n=5
obj.print_name(n,n)