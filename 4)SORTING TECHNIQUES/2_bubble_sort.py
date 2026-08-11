class Solution(object):
    def bub_sort(self, arr):
        n = len(arr)

        for i in range(n - 1, 0, -1):
            swapped = False

            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            if not swapped:
                break

        return arr
    
obj = Solution()

arr = [5,4,3,2,1]

print(obj.bub_sort(arr))


#Recursive bubble sort
class Solution:
    def bubble_sort(self, arr, n):

        # Base case
        if n == 1:
            return

        # One pass: largest element moves to the end
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

        # Recursively sort remaining array
        self.bubble_sort(arr, n - 1)


obj = Solution()

arr = [5, 4, 3, 2, 1]

obj.bubble_sort(arr, len(arr))

print(arr)