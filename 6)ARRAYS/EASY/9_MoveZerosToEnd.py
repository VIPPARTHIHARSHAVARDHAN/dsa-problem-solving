#brute force solution
class Solution(object):
    def moveZeroes(self, nums):
        temp = []

        # Store all non-zero elements
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])

        # Copy non-zero elements back
        for i in range(len(temp)):
            nums[i] = temp[i]

        # Fill remaining positions with zeros
        for i in range(len(temp), len(nums)):
            nums[i] = 0
            
            
#optimal solution
class Solution(object):
    def moveZeroes(self, nums):
        j = -1

        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break

        # No zero found
        if j == -1:
            return nums

        for i in range(j + 1, len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1

        return nums
obj=Solution()
nums=[1,2,0,3,0,4]
print(obj.moveZeroes(nums))