class Solution(object):
    def mergesort(self, arr,low,high):
        if low>=high:
            return 
        mid=(low+high)//2
        self.mergesort(arr,low,mid)
        self.mergesort(arr,mid+1,high)
        self.merge(arr,low,mid,high)
    def merge(self,arr,low,mid,high):
        temp=[]
        left=low
        right=mid+1
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        
        while left<=mid:
            temp.append(arr[left])
            left+=1
        
        while right<=high:  
            temp.append(arr[right])
            right+=1 
        for i in range(len(temp)):
            arr[low + i] = temp[i]
        
      
obj = Solution()

arr = [5,4,3,2,1]

obj.mergesort(arr,0,len(arr)-1)
print(arr)