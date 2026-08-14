
#brute force solution

class Solution(object):
    def Secondlargest(self,arr):
        arr.sort()
        largest=arr[-1]
        for i in range(len(arr)-2,-1,-1):
            
            if arr[i]!=largest:
                return arr[i]
        return -1       
        
obj=Solution()
arr=[4,9,32,94]
print(obj.Secondlargest(arr))

#optimal solution
class Solution(object):
    def Secondlargest(self, arr):
        largest = arr[0]
        secondlargest = -1

        for i in range(1, len(arr)):
            if arr[i] > largest:
                secondlargest = largest
                largest = arr[i]
            elif arr[i] > secondlargest and arr[i] != largest:
                secondlargest = arr[i]

        return secondlargest


obj = Solution()
arr = [95, 9, 32, 94]
print(obj.Secondlargest(arr))