class Solution(object):
    def longestsubarray(self, nums,k):
        longestsubarr=0
        for i in range(len(nums)):
            sum=0
            for j in range(i,len(nums)):
                
                
                sum+=nums[j]
                if (sum==k):
                    longestsubarr=max(longestsubarr,j-i+1)
        return longestsubarr
obj = Solution()

nums = [1, 2, 1, 1, 1]
k = 3

print(obj.longestsubarray(nums, k))
    #O(n cube)
    
    #optimal
    
class Solution(object):
    def longestsubarray(self, nums,k):
        total=0
        left=0
        longlen=0
        for right in range(len(nums)):
            total+=nums[right]
            while total>k:
                total-=nums[left]
                left+=1
            if total==k:
                
                 longlen=max(longlen,right-left+1)
        return longlen
    
obj = Solution()

nums = [1, 2, 1, 1, 1]
k = 3

print(obj.longestsubarray(nums, k))