#brute force
class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1

        for day in range(min(bloomDay), max(bloomDay) + 1):
            bouquets = 0
            flowers = 0

            for i in range(len(bloomDay)):
                if bloomDay[i] <= day:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

            if bouquets >= m:
                return day

        return -1


#optimal solution
class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        low = min(bloomDay)
        high=max(bloomDay)
        while low<=high:
            mid=(low+high)//2
            flowers=0
            bouquets=0
            for day in bloomDay:
                if day<=mid:
                    flowers+=1
                    if flowers==k:
                        bouquets+=1
                        flowers=0
                else:
                    flowers=0
            if bouquets>=m:
                high=mid-1
            else:
                low= mid+1
        return low
obj = Solution()

bloomDay = [1, 10, 3, 10, 2]
m = 3
k = 1

answer = obj.minDays(bloomDay, m, k)

print(answer)
