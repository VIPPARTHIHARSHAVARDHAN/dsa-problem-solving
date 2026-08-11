class Solution(object):
    def peak(self, nums):
        n=len(nums)
        if nums[0]>nums[1]:
            return nums[0]
        if nums[n-1]>nums[n-2]:
            return nums[n-1]
        low=1
        high=n-2
        while low<=high:
            mid=(low+high)//2
            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return nums[mid]
            if nums[mid]>nums[mid+1]  and nums[mid-1] > nums[mid]:
                high=mid-1
            else:
                low=mid+1
        return -1
        

obj = Solution()

nums = [1,2,3,4,5,6,4]

print(obj.peak(nums))   

        
        