class Solution(object):
    def fc(self, nums, target):
        low = 0
        high = len(nums) - 1
        floor=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=target:
                floor=nums[mid]
                low=mid+1
            else:
                high=mid-1
        
        low = 0
        high = len(nums) - 1
        ceil=-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                ceil=nums[mid]
                high=mid-1
            else:
                low=mid+1   
             
        return [floor,ceil]
obj = Solution()

nums = [-1, 0, 3, 5, 9, 12]
target = 11

print(obj.fc(nums, target))