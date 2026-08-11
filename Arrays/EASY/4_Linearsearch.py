class Solution(object):
    def LinearSearch(self, nums,element):
        for i in range(len(nums)):
            if(nums[i]==element):
                return i
        return -1
obj=Solution()
nums=[1,2,3,4,4]
print(obj.LinearSearch(nums,3))
        