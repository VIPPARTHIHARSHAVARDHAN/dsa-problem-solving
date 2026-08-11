class Solution(object):
    def numofsub(self, arr,k):
        
        count=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                sum=0
                for m in range(i,j+1):
                    sum+=arr[m]
                if sum==k:
                    count+=1
        return count
obj = Solution()

arr = [1, 2, 1, 1, 1]
k = 3

print(obj.numofsub(arr, k))


#better solution 
class Solution(object):
    def numofsub(self, arr,k):
        
        count=0
        for i in range(len(arr)):
            sum=0
            for j in range(i,len(arr)):
                
                
                sum+=arr[j]
                if sum==k:
                    count+=1
        return count
obj = Solution()

arr = [1, 2, 1, 1, 1]
k = 3

print(obj.numofsub(arr, k))


#optimal solution
class Solution(object):
    def subarraySum(self, nums, k):
        pref_sum=0
        count=0
        hmp={0:1}
        for num in nums:
            pref_sum+=num
            if pref_sum-k in hmp:
                count+=hmp[pref_sum-k]
            hmp[pref_sum]=hmp.get(pref_sum,0)+1
        return count
obj = Solution()

nums = [1, 2, 1, 1, 1]
k = 3

print(obj.subarraySum(nums, k))