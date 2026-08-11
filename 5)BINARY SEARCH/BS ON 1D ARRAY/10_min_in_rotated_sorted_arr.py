class Solution(object):
    def minrotate(self, nums):
        low = 0
        high=len(nums)-1
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            
            if nums[low] <=nums[mid]:
                ans=min(nums[low],ans)
                
                low=mid+1
                
            else:
                
                ans=min(ans,nums[mid])
                high=mid-1
            
                
        return ans
                
obj = Solution()

nums = [4,5,6,1,2,3]

print(obj.minrotate(nums))           
                