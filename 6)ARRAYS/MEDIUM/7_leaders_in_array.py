class Solution(object):
    def leaders(self,arr):
        ans=[]
        for i in range(len(arr)):
            leader=True
            for j in range(i+1,len(arr)):
                if arr[j]>arr[i]:
                    leader=False
                    break
            if leader==True:
                ans.append(arr[i])
        return ans
obj=Solution()
arr=[1,2,3,10,8,7]
print(obj.leaders(arr))

# Optimal solution
class Solution(object):
    def leaders(self,arr):
        maximum=float('-inf')
        ans=[]
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>maximum:
                ans.append(arr[i])
                maximum=max(maximum,arr[i])
        #if they ask with array order
        ans.reverse()
        #if they ask sort order
        #ans.sort()
        return ans
                
obj=Solution()
arr=[1,2,3,10,8,7]
print(obj.leaders(arr))        