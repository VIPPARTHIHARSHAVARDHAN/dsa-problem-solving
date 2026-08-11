#brute force solution

class Solution(object):
    def TwoSum(self,arr,target):
        
        for i in range(len(arr)):
            for j in range (i+1,len(arr)):
                
                if(arr[i]+arr[j]==target):
                    return i,j
                
        
obj = Solution()

arr = [2, 7, 11, 15]
target = 9

print(obj.TwoSum(arr, target))  

#Better solution using hasing
class Solution(object):
    def TwoSum(self, arr, target):
        hashmap={}
        for i in range(len(arr)):
            compliment=target-arr[i]
            if compliment in hashmap:
                 return hashmap[compliment],i
            hashmap[arr[i]]=i
obj = Solution()

arr = [2, 7, 11, 15]
target = 9

print(obj.TwoSum(arr, target))


#optimal solution is only for yes/no type in that we cant get indexes
class Solution(object):
    def TwoSum(self, arr, target):
        arr.sort
        left=0
        right=len(arr)-1
        while left<right:
            total=arr[left]+arr[right]
            if total==target:
                return True
            #    return arr[left],arr[right] if we want numbers
            elif target<total:
                right-=1
            else:
                left+=1
obj = Solution()

arr = [2, 7, 11, 15]
target = 9

print(obj.TwoSum(arr, target))
            
                
        