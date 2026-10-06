class Solution(object):
    def moveZeroes(self, nums):
        j = 0

        for i in range(len(nums)):
            if nums[i] <0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return nums


obj = Solution()
nums = [1, 2, -2, 3, -1, 4]
print(obj.moveZeroes(nums))