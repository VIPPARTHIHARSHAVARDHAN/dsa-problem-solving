#brute force
class Solution(object):
    def findKthPositive(self, arr, k):
        for i in range(len(arr)):
            if arr[i] <= k:
                k += 1
            else:
                break

        return k


obj = Solution()

arr = [2, 3, 4, 7, 11]
k = 5

print(obj.findKthPositive(arr, k))

#optimal solution
class Solution(object):
    def findKthPositive(self, arr, k):
        low = 0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            missing=arr[mid]-(mid+1)
            if missing<k:
                low=mid+1
            else:
                high=mid-1
        return low+k

obj = Solution()

arr = [2, 3, 4, 7, 11]
k = 5

print(obj.findKthPositive(arr, k))

