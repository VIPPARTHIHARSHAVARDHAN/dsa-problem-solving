class Solution(object):
    def rotate2(self, nums, target):
        low = 0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target :
                return True
            if nums[mid]==nums[low] and nums[high]==nums[mid]:
                high=high-1
                low=low+1
                continue
            
            if nums[low] <=nums[mid]:
                
                if nums[low]<=target and target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
            else:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
        return -1
                
obj = Solution()

nums = [3,1,2,3,3,3,3]
target = 1

print(obj.rotate2(nums, target))           
                