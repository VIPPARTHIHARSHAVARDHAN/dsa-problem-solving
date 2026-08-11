class Solution(object):
    def occurence(self, nums, target):
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
            return 0
        count=last-first+1

        return count
obj = Solution()

nums = [-1, 0, 3, 5, 9,9, 12]
target = 9

print(obj.occurence(nums, target))

