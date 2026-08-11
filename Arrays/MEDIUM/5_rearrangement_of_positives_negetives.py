#brute force solution

class Solution(object):
    def rearrangement(self, arr):
        postemp = []
        negtemp = []

        # Store positive and negative numbers
        for i in range(len(arr)):
            if arr[i] >= 0:
                postemp.append(arr[i])
            else:
                negtemp.append(arr[i])

        # Rearrange alternatively
        for i in range(len(arr) // 2):
            arr[2 * i] = postemp[i]
            arr[2 * i + 1] = negtemp[i]

        return arr


# Object Creation
obj = Solution()

arr = [3, 1, -2, -5, 2, -4]

print(obj.rearrangement(arr))

#optimal solution for type 1
class Solution(object):
    def rearrangement(self, arr):
        ans=[0]*len(arr)
        pos=0
        neg=1
        for i in range(len(arr)):
            if arr[i]>=0:
                ans[pos]=arr[i]
                pos+=2
            else:
                ans[neg]=arr[i]
                neg+=2
        return ans
obj=Solution()
arr=[-1,2,3,-2]
print(obj.rearrangement(arr))


# only bruteforce solution for type=2 where pos!=neg no optimal for this
class Solution(object):
    def rearrangement(self, arr):
        positive=[]
        negetive=[]
        for i in range(len(arr)):
            if arr[i]>=0:
                positive.append(arr[i])
            else:
                negetive.append(arr[i])
        i=0
        j=0
        result=[]
        while i<len(positive) and j<len(negetive):
            result.append(positive[i])
            result.append(negetive[j])
            i+=1
            j+=1
        while i<len(positive):
            result.append(positive[i])
            i+=1
        while j<len(negetive):
            result.append(negetive[j])
            j+=1
        return result
    
            
obj=Solution()
arr=[-1,2,3,4,-2]
print(obj.rearrangement(arr))          
            
