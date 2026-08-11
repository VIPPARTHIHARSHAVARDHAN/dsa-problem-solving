class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)

        for i in range(n + 1):
            found = False

            for j in range(n):
                if nums[j] == i:
                    found = True
                    break

            if found==False:
                return i


obj = Solution()
nums = [3, 0, 1]
print(obj.missingNumber(nums))


#optimal solution
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total=(n*(n+1))//2
        sum_arr=0
        for i in range(n):
            sum_arr+=nums[i]
            
            
            
        return total-sum_arr


obj = Solution()
nums = [3, 0, 1]
print(obj.missingNumber(nums))
