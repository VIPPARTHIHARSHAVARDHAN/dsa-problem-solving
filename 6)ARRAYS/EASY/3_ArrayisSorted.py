class Solution(object):
    def isSorted(self,arr):
        
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                continue
            else:
                return False   
        return True
obj=Solution()
arr=[4,9,32,94]
print(obj.isSorted(arr))