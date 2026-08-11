class Solution(object):

    def print_base(self, count):
        if count == 4:
            return

        print(count)
        self.print_base(count + 1)

obj = Solution()
obj.print_base(0)


#using instance variable
class Solution(object):

    def __init__(self):
        self.count = 0

    def print_base(self):
        if self.count == 4:
            return

        print(self.count)
        self.count += 1
        self.print_base()

obj = Solution()
obj.print_base()