class Solution(object):
    def arm(self, n):
        temp=n
        arm=0
        digits=self.counter(n)
        while n>0:
            lastdigit=n%10
            cube=lastdigit**digits
            arm+=cube
            n=n//10
        if arm==temp:
            return True
        return False
    def counter(self,n):
        count=0
        while n>0:
            count+=1
            n=n//10
        return count
            
obj=Solution()
n=371
print(obj.arm(n))