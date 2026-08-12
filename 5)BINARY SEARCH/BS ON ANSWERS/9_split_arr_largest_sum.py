class Solution(object):
    def splitArray(self, nums, k):
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low + high) // 2
            current = 0
            subarrays = 1

            for i in range(len(nums)):
                if current + nums[i] <= mid:
                    current += nums[i]
                else:
                    subarrays += 1
                    current = nums[i]

            if subarrays <= k:
                high = mid - 1
            else:
                low = mid + 1

        return low


obj = Solution()

nums = [7, 2, 5, 10, 8]
k = 2

print(obj.splitArray(nums, k))