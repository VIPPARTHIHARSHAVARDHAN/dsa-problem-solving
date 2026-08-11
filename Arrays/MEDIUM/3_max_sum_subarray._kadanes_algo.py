#brute force solution

class Solution(object):
    def maxsumsubarr(self, arr):
        maximum = float('-inf')

        for i in range(len(arr)):
            for j in range(i, len(arr)):
                curr_sum = 0
                for k in range(i, j + 1):
                    curr_sum += arr[k]
                    maximum = max(curr_sum, maximum)

        return maximum
    
#better solution
class Solution(object):
    def maxsumsubarr(self, arr):
        maximum = float('-inf')

        for i in range(len(arr)):
            curr_sum = 0
            for j in range(i, len(arr)):
                
                curr_sum += arr[j]
                maximum = max(curr_sum, maximum)
        return maximum
    
#optimal solution only when max sum required
class Solution(object):
    def maxsumsubarr(self, arr):
        maximum=float('-inf')
        sum=0
        for i in range(len(arr)):
            if sum<0:
                sum=0           
            sum+=arr[i]
            maximum=max(maximum,sum)
        return maximum
obj=Solution()
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(obj.maxsumsubarr(arr))







#optimal solution to give subarr of maximum sum
class Solution(object):
    def maxsumsubarr(self, arr):
        maximum = float('-inf')
        curr_sum = 0

        start = 0
        ans_start = 0
        ans_end = 0

        for i in range(len(arr)):
            if curr_sum == 0:
                start = i

            curr_sum += arr[i]

            if curr_sum > maximum:
                maximum = curr_sum
                ans_start = start
                ans_end = i

            if curr_sum < 0:
                curr_sum = 0

        return maximum, ans_start, ans_end


obj = Solution()
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(obj.maxsumsubarr(arr))