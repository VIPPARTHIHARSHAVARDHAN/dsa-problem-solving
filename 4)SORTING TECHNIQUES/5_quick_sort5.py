class Solution(object):
    def qsort(self, arr,low,high):
        if low<high:
            partition_index=self.fun(arr,low,high)
            self.qsort(arr,low,partition_index-1)
            self.qsort(arr,partition_index+1,high)
    def fun(self,arr,low,high):
        i=low
        j=high
        pivot=arr[low]
        while(i<j):
            while i<=high and arr[i]<=pivot:
                i+=1
            while j>=low and arr[j]>pivot:
                j-=1
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        arr[low],arr[j]=arr[j],arr[low]
        return j    
   
obj = Solution()

arr = [5,4,3,2,1]

obj.qsort(arr,0,len(arr)-1)
print(arr)