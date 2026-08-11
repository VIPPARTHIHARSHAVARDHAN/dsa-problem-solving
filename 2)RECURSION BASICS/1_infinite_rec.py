# This is a standalone (global) function.
# Python stores it with the name 'print_one'.

def print_one():
    print(1)

    # Calls the same global function again.
    # No object is needed because it is not inside a class.
    print_one()

# First function call starts from here.
print_one()






class Solution(object):

    # This is a method, not a standalone function.
    # It belongs to the Solution class.
    def print_one(self):
        print(1)

        # Calls the same method using the current object.
        # 'self' refers to the object that called this method.
        self.print_one()

# Create an object of the Solution class.
obj = Solution()

# First method call starts from here.
obj.print_one()