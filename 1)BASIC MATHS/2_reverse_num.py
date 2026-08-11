class Solution(object):
    def revnum(self, n):
        rev=0
        while n>0:
            lastdigit=n%10
            
            rev=rev*10
            rev+=lastdigit
            n=n//10
        return rev
obj=Solution()
n=32830

print(obj.revnum(n))

#leetcode 7
class Solution(object):
    def reverse(self, x):
        sign=-1 if x<0 else 1
        x=abs(x)
        rev=0
        while(x>0):
            lastdig=x%10
            rev=rev*10
            rev+=lastdig
            x=x//10
        rev*=sign
        if rev<-2**31 or rev>2**31:

            return 0
        return rev


        