class Solution(object):
    def ins_sort(self, arr):
        for i in range(len(arr)):
            j=i
            while(j>0 and arr[j-1]>arr[j]):
                arr[j-1],arr[j]=arr[j],arr[j-1]
                j-=1
        return arr
obj = Solution()

arr = [5,4,3,2,1]

print(obj.ins_sort(arr))




#insertion sort using recursion
class Solution:

    def ins_sort(self, arr, i):

        # Base case
        if i == len(arr):
            return

        j = i

        # Same logic as your while loop
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

        # Recursive call for next index
        self.ins_sort(arr, i + 1)


obj = Solution()

arr = [5, 4, 3, 2, 1]

obj.ins_sort(arr, 0)

print(arr)