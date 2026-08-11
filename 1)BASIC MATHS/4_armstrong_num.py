class Solution(object):
    def arm(self, n):
        temp=n
        arm=0
        count=0
        while n>0:
            lastdigit=n%10
            cube=lastdigit**3
            arm+=cube
            n=n//10
        if arm==temp:
            return True
        return False
obj=Solution()
n=371
print(obj.arm(n))