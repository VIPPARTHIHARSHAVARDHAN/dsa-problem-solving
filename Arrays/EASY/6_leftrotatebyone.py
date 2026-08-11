#brute force/optimal
class Solution(object):
    def LeftRotate(self,arr):
        temp=arr[0]
        for i in range(1,len(arr)):
            arr[i-1]=arr[i]
        arr[-1]=temp
        return arr

obj=Solution()
arr=[4,9,9,32,94]
print(obj.LeftRotate(arr))    
