class Solution(object):
    def sqrt(self, n):
        if n == 0:
            return 0

        low = 1
        high = n
        ans = 1

        while low <= high:
            mid = (low + high) // 2

            if mid * mid <= n:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans


obj = Solution()
print(obj.sqrt(25))