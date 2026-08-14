#brute force solution
class Solution(object):
    def sort_0_1_2(self,arr):
        count0=0
        count1=0
        count2=0
        for i in range(len(arr)):
            if arr[i]==0:
                count0+=1
            elif arr[i]==1:
                count1+=1
            else:
                count2+=1
        for i in range(count0):
            arr[i]=0
        for i in range(count0,count0+count1):
            arr[i]=1
        for i in range(count0+count1,len(arr)):
            arr[i]=2
        return arr
        
obj = Solution()

arr = [2, 0, 2, 1, 1, 0]

print(obj.sort_0_1_2(arr)) 

#optimal #dutch national flag algorithm
class Solution(object):
    def sort_0_1_2(self,arr):
        low=0
        high=len(arr)-1
        mid=0
        while(mid <= high):
            if arr[mid]==0:
                arr[low],arr[mid]=arr[mid],arr[low]
                low+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            else:
                
                arr[mid],arr[high]=arr[high],arr[mid]
                high-=1
        return arr
obj = Solution()

arr = [2, 0, 2, 1, 1, 0]

print(obj.sort_0_1_2(arr))
            