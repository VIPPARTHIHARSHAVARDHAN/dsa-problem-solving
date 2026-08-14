class Solution(object):
    def findMaxRow(self, arr):
        n = len(arr)
        m = len(arr[0])

        max_count = -1
        row_index = -1

        for i in range(n):
            count = 0

            for j in range(m):
                if arr[i][j] == 1:
                    count += 1

            if count > max_count:
                max_count = count
                row_index = i

        return row_index


arr = [
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

obj = Solution()
print(obj.findMaxRow(arr))

#optimal Solution
class Solution(object):
    def findMaxRow(self, arr):
        n=len(arr)
        m=len(arr[0])
        max_count=-1
        row_index=-1
        for i in range(n):
            low=0
            high=m-1
            while low<=high:
                mid=(low+high)//2
                if arr[i][mid]>=1:
                    high=mid-1
                else:
                    low=mid+1
            count= m-low
            if count>max_count:
                max_count=count
                row_index=i
        return row_index
arr = [
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

obj = Solution()
print(obj.findMaxRow(arr))