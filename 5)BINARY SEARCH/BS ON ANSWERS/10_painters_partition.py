class Solution(object):
    def minTime(self, arr, k):
        low = max(arr)
        high = sum(arr)

        while low <= high:
            mid = (low + high) // 2

            current = 0
            painters = 1

            for i in range(len(arr)):
                if current + arr[i] <= mid:
                    current += arr[i]
                else:
                    painters += 1
                    current = arr[i]

            if painters <= k:
                high = mid - 1
            else:
                low = mid + 1

        return low


obj = Solution()

arr = [10, 20, 30, 40]
k = 2

print(obj.minTime(arr, k))