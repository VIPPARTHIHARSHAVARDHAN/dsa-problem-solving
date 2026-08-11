class Solution(object):
    def appearOnce(self, nums):
        
        for i in range(len(nums)):
            count=0
            for j in range(0,len(nums)):
                if nums[j]==nums[i]:
                    count+=1
            if count==1:
                return nums[i]
                    
obj=Solution()
nums=[1,1,2,3,2,3,5]
print(obj.appearOnce(nums))

#optimal using xor
class Solution(object):
    def appearOnce(self, nums):
        xor=0
        
        for i in range(len(nums)):
            xor^=nums[i]
        return xor
obj=Solution()
nums=[1,1,2,3,2,3,5]
print(obj.appearOnce(nums))