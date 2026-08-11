#model 1  question
class Solution(object):
    def pascal(self, row,col):
        n=row-1
        r=col-1
        return self.ncr(n,r)
        
    def ncr(self,n,r):
        
        res=1
        for i in range(r):
            res*=n-i
            res//=i+1
        return res
obj = Solution()
print(obj.pascal(5, 3))

#model 2 question
class Solution(object):
    def pascal(self, n):
        result = [1]
        ans = result[0]

        for i in range(1, n+1):
            ans = ans * ((n - i)+1)
            ans = ans // i
            result.append(ans)

        return result


obj = Solution()
print(obj.pascal(5))
    
#model 3 better and optimal
class Solution(object):
    def generateRow(self, row):
        result=[1]
        ans=result[0]
        for i in range(1,row):
            ans = ans * (row - i)
            ans = ans // i
            result.append(ans)
        return result
    def pascal(self,n):
        triangle=[]
        for row in range(1,n+1):
            triangle.append(self.generateRow(row))
        return triangle
obj = Solution()
triangle = obj.pascal(5)

for row in triangle:
    print(row)
        
        
        
        


    
    
    
    
    
    
    
    
    