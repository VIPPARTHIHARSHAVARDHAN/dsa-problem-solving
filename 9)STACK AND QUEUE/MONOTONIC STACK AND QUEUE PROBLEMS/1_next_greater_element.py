#bruteforce Solution
def nextGreaterElement(arr):
    n = len(arr)
    nge = [-1] * n

    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                nge[i] = arr[j]
                break

    return nge


arr = [6, 0, 8, 1, 3]

print(nextGreaterElement(arr))


#optimal solution using dcreasing monotonic
def nextGreaterElement(arr):
    n = len(arr)
    nge = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):

        # Remove elements smaller than or equal to arr[i]
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # Top of stack is the next greater element
        if stack:
            nge[i] = stack[-1]

        # Push current element
        stack.append(arr[i])

    return nge


arr = [6, 0, 8, 1, 3]

print(nextGreaterElement(arr))




#leetcode 496
class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nge = {}

        for i in range(len(nums2) - 1, -1, -1):

            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                nge[nums2[i]] = stack[-1]
            else:
                nge[nums2[i]] = -1

            stack.append(nums2[i])

        ans = []

        for num in nums1:
            ans.append(nge[num])

        return ans