class Solution(object):
    def search(self, nums, target):
        low=0
        high=len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                low=mid+1
            else:
                high=mid-1
        return -1
            
obj = Solution()

nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(obj.search(nums, target))




#using recursion
class Solution(object):
    def binarySearch(self, nums, target, low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(nums, target, mid + 1, high)
        else:
            return self.binarySearch(nums, target, low, mid - 1)

    def search(self, nums, target):
        return self.binarySearch(nums, target, 0, len(nums) - 1)


# Object creation
obj = Solution()

nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(obj.search(nums, target))
        
        