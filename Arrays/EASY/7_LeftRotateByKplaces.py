#brute force/optimal
class Solution(object):
    def LeftRotate(self,arr,d):
        temp=arr[:d]
        for i in range(d,len(arr)):
            arr[i-d]=arr[i]
        j=0
        for i in range(len(arr)-d,len(arr)):
            arr[i]=temp[j]
            j+=1
        # or we can write like this also
        #for i in range(len(arr)-d,len(arr)):
            #arr[i]=temp[i-(n-d)]
           
        return arr
        

obj=Solution()
arr=[4,9,9,32,94]
d=3
print(obj.LeftRotate(arr,d))    


#optimal solution
class Solution(object):
    def reverse(self,arr,start,end):
        while start < end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    def LeftRotate(self,arr,d):
        n=len(arr)
        d=d%n
        self.reverse(arr,0,d-1)
        self.reverse(arr,d,n-1)
        self.reverse(arr,0,n-1)
        return arr
    
obj=Solution()
arr=[1,2,3,4,5]
d=54
print(obj.LeftRotate(arr,d))     
    
    
    #easy code using slicing
class Solution(object):
    def LeftRotate(self, arr, d):
        n = len(arr)
        d = d % n

        arr[:] = arr[d:] + arr[:d]
        return arr


obj = Solution()

arr = [4, 9, 9, 32, 94]
print(obj.LeftRotate(arr, 3))
            