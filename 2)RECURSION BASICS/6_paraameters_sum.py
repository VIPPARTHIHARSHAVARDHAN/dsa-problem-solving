class Solution:
    def print_sum(self, i, sum):
        if i ==0:
            print(sum) 
            return

        self.print_sum(i -1, sum+i)   # Go till the end
                        # Print while coming back

obj = Solution()
obj.print_sum(5, 0)