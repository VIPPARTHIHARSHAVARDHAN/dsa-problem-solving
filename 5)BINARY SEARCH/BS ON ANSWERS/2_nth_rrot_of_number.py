class Solution(object):
    def sqrt(self, n, m):
        if n == 0:
            return 0

        low = 1
        high = m

        while low <= high:
            mid = (low + high) // 2

            if mid ** n == m:
                return mid
            elif mid ** n < m:
                low = mid + 1
            else:
                high = mid - 1

        low = high
        high = low + 1
        ans = low
        #if exact root does not exist check for decimal

        for i in range(30):
            mid = (low + high) / 2

            if mid ** n < m:
                ans = mid
                low = mid
            else:
                high = mid
        

        return round(ans,2)


obj = Solution()

print(obj.sqrt(3, 27))
print(obj.sqrt(3, 20))