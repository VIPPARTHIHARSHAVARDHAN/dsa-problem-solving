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


#is array is sorted even rotated by k places
class Solution(object):
    def check(self, nums):
        n=len(nums)
        count=0
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                count+=1
        return count<=1
    