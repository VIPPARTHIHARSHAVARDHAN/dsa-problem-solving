class Solution:
    def print_reverse(self,arr, l,r):
        if l >=r:
            return 
             
        arr[l], arr[r] = arr[r], arr[l]
        self.print_reverse(arr,l+1,r-1)
        

        

obj = Solution()
arr = [1, 2, 3, 4, 5]
obj.print_reverse(arr,0,len(arr)-1)
print(arr)


#using only i
class Solution:
    def reverse_array(self, arr, i):
        n = len(arr)

        if i >= n // 2:
            return

        arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]
        self.reverse_array(arr, i + 1)

obj = Solution()

arr = [1, 2, 3, 4, 5]
obj.reverse_array(arr, 0)

print(arr)
