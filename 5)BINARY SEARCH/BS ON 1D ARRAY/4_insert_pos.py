class Solution(object):
    def pos(self, nums, target):
        low = 0
        high = len(nums) - 1
        ans = len(nums)

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans


obj = Solution()

nums = [-1, 0, 3, 5, 9, 12]
target = 9

print(obj.pos(nums, target))