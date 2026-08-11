class Solution(object):
    def fl(self, nums, target):
        low = 0
        high = len(nums) - 1
        first = len(nums)

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                first = mid
                high = mid - 1
            else:
                low = mid + 1

        low = 0
        high = len(nums) - 1
        last = len(nums)

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                last = mid
                high = mid - 1
            else:
                low = mid + 1

        last = last - 1

        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        return [first, last]
obj = Solution()

nums = [-1, 0, 3, 5, 9, 12]
target = 11

print(obj.fc(nums, target))


#without using lower bound and uppper bound concept
class Solution(object):
    def searchRange(self, nums, target):

        # Find First Occurrence
        low = 0
        high = len(nums) - 1
        first = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                first = mid
                high = mid - 1      # Search on the left
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        # Find Last Occurrence
        low = 0
        high = len(nums) - 1
        last = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                last = mid
                low = mid + 1       # Search on the right
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [first, last]


obj = Solution()

nums = [5, 7, 7, 8, 8, 10]
target = 8

print(obj.searchRange(nums, target))