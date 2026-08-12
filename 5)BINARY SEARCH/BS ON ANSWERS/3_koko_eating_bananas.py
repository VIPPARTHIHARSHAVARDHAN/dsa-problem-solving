#brute force solution
import math
class Solution(object):

    def func(self, arr, hourly):
        totalhrs = 0

        for i in range(len(arr)):
            totalhrs += math.ceil(arr[i]/hourly)

        return totalhrs

    def minEatingSpeed(self, piles, h):
        for i in range(1, max(piles) + 1):
            reqTime = self.func(piles, i)

            if reqTime <= h:
                return i

        return -1


obj = Solution()

piles = [3, 6, 7, 11]
h = 8

print(obj.minEatingSpeed(piles, h))


#optimal
import math
class Solution(object):
    def minEatingSpeed(self,piles,h):
        low=1
        high=max(piles)
        while low<=high:
            mid=(low+high)//2
            req_time=self.fun(piles,mid)
            if req_time<=h:
                high=mid-1
            else:
                low = mid+1
        #low always poins to min value at last 
        return low
    def fun(self,arr,hourly):
        total_time=0
        for i in range(len(arr)):
            
            total_time+=math.ceil(arr[i]/hourly)  
            #we can use this logic also
            #tota_time+=(arr[i]+hourly-1)//hourly
        return total_time  


obj = Solution()

piles = [3, 6, 7, 11]
h = 8

print(obj.minEatingSpeed(piles, h))



