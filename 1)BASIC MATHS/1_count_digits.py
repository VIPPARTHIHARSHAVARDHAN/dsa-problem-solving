class Solution(object):
    def countdig(self, n):
        count=0
        while n>0:
            count+=1
            n=n//10
        return count
    def arm(self,n):
        temp=n
        digits=self.countdig(n)
        arm=0
        while n>0:
            lastdigit=n%10
            arm+=lastdigit**digits
            n//=10   
        return arm==temp     
obj=Solution()
n=9474
print(obj.arm(n))