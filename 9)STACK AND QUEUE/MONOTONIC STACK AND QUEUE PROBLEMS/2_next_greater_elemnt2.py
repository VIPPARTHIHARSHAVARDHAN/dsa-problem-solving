#brute force
class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        nge = [-1] * n

        for i in range(n):
            for j in range(1, n):
                index = (i + j) % n

                if nums[index] > nums[i]:
                    nge[i] = nums[index]
                    break

        return nge
    
    
#optimal solution
def nextGreaterElement(arr):
    n = len(arr)
    nge = [-1] * n
    stack = []

    for i in range(2 * n - 1, -1, -1):

        # Get circular index
        index = i % n

        while stack and stack[-1] <= arr[index]:
            stack.pop()

        # Only store answer for original array positions
        if i < n:
            if stack:
                nge[index] = stack[-1]

        stack.append(arr[index])

    return nge


arr = [6, 0, 8, 1, 3]

print(nextGreaterElement(arr))