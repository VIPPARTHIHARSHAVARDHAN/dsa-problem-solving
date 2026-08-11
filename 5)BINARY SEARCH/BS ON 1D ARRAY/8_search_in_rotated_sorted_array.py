class Solution(object):
    def rotate(self, nums, target):
        low = 0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
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

nums = [4,5,6,0,1,2,3]
target = 0

print(obj.rotate(nums, target))           
                