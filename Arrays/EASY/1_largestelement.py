#brute force
class Solution(object):
    def largest(self,arr):
        arr.sort()
        return arr[-1]

obj=Solution()
arr=[4,9,32,94]
print(obj.largest(arr))

#optimal
class Solution(object):
    def largest(self,arr):
        largest=arr[0]
        for i in range(len(arr)):
            if arr[i]>largest:
                largest=arr[i]
        return largest
obj=Solution()
arr=[4,9,32,94]
print(obj.largest(arr))