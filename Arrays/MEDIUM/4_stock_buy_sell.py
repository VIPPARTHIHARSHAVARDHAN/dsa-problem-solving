class Solution(object):
    def stockbuysell(self, arr):
        profit = 0
        minimum = arr[0]

        for i in range(1, len(arr)):
            cost = arr[i] - minimum
            profit = max(profit, cost)
            minimum = min(minimum, arr[i])

        return profit


# Object creation
obj = Solution()

# Input array (stock prices)
arr = [7, 1, 5, 3, 6, 4]

# Function call
result = obj.stockbuysell(arr)

# Output
print(result)