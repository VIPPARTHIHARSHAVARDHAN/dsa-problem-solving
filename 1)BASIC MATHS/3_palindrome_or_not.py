class Solution(object):
    def palin(self, n):
        temp=n
        rev=0
        while n>0:
            lastdigit=n%10
            
            rev=rev*10
            rev+=lastdigit
            n=n//10
        if rev==temp:
            return True
        return False
obj=Solution()
n=323

print(obj.palin(n))