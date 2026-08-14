class Solution(object):
    def nextpermutation(self, arr):
        index=-1
        for i in range(len(arr)-2,-1,-1):
            if arr[i]<arr[i+1]:
                index=i
                break
            
        if index==-1:
            arr.reverse()
            return arr
            
        for i in range(len(arr)-1,index,-1):
            if arr[i]>arr[index]:
                arr[i],arr[index]=arr[index],arr[i]
                break
        arr[index+1:]=reversed(arr[index+1:])
        return arr
obj = Solution()

arr = [2,1,5,4,3,0,0]
print(obj.nextpermutation(arr))
        
            