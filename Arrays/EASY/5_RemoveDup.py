# brute force
class Solution(object):
    def Duplicates(self,arr):
        Unique=list(set(arr))
        return Unique
obj=Solution()
arr=[4,9,9,32,94]
print(obj.Duplicates(arr))    

#optimal solution

class Solution(object):
    def Duplicates(self,arr):
        i=0
        for j in range(1,len(arr)):
            if arr[j]!=arr[i]:
                i+=1
                arr[i]=arr[j]
                #elements,no.elements
        return arr[:i+1],i+1
        
            
obj=Solution()
arr=[3,3,2,2,1,1]
print(obj.Duplicates(arr))    
         
         
#leetcode26
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i=0
        for j in range(1,len(nums)):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1