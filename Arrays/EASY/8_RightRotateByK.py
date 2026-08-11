#brute force solution
class Solution(object):
    def RightRotate(self, arr, d):
        n = len(arr)
        d = d % n

        # Store last d elements
        temp = arr[n-d:]

        # Shift remaining elements to the right
        for i in range(n-d-1, -1, -1):
            arr[i+d] = arr[i]

        # Copy temp to the beginning
        j = 0
        for i in range(d):
            arr[i] = temp[j]
            j += 1

        return arr


obj = Solution()
arr = [4,9,9,32,94]
d = 3

print(obj.RightRotate(arr, d))

#optimal solution 
class Solution(object):
    def reverse(self,arr,start,end):
        while start < end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    def LeftRotate(self,arr,d):
        n=len(arr)
        d=d%n
        self.reverse(arr,0,n-d-1)
        self.reverse(arr,n-d,n-1)
        self.reverse(arr,0,n-1)
        return arr
    
obj=Solution()
arr=[1,2,3,4,5]
d=2
print(obj.LeftRotate(arr,d)) 


#easy code using slicing
class Solution(object):
    def RightRotate(self, arr, d):
        n = len(arr)
        d = d % n

        arr[:] = arr[-d:] + arr[:-d]
        return arr


obj = Solution()

arr = [4, 9, 9, 32, 94]
print(obj.RightRotate(arr, 3))