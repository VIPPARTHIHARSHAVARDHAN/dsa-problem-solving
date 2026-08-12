class Solution(object):
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)

        for capacity in range(low, high + 1):
            current = 0
            count_days = 1

            for i in range(len(weights)):
                if current + weights[i] <= capacity:
                    current += weights[i]
                else:
                    count_days += 1
                    current = weights[i]

            if count_days <= days:
                return capacity

        return -1


obj = Solution()

weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5

print(obj.shipWithinDays(weights, days))

#optimal solution
class Solution(object):
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (low + high) // 2
            current = 0
            req_days = 1

            for i in range(len(weights)):
                if current + weights[i] <= mid:
                    current += weights[i]
                else:
                    req_days += 1
                    current = weights[i]

            if req_days <= days:
                high = mid - 1
            else:
                low = mid + 1

        return low


obj = Solution()
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5

print(obj.shipWithinDays(weights, days))                
                    
                
            