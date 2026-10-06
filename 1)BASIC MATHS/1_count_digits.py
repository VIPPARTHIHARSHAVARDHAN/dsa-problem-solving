class Solution(object):
    def countdig(self, n):
        count=0
        while n>0:
           
            
            count+=1
            n=n//10
        return count
       
obj=Solution()
n=9474
print(obj.countdig(n))