#brute force solution
import math

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        for d in range(1, max(nums) + 1):
            total = 0

            for i in range(len(nums)):
                total += math.ceil(nums[i] / d)

            if total <= threshold:
                return d

        return -1


obj = Solution()

nums = [1, 2, 5, 9]
threshold = 6

print(obj.smallestDivisor(nums, threshold))

#optimal solution
import math

class Solution(object):
    def smallestDivisor(self, nums, threshold):
        low=1
        high=max(nums)
        while low<=high:
            mid=(low+high)//2
            sum=0
            for i in range(len(nums)):
                sum+=math.ceil(nums[i]/mid)
            if sum<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low
obj = Solution()

nums = [1, 2, 5, 9]
threshold = 6

print(obj.smallestDivisor(nums, threshold))              
        
