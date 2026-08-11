class Solution(object):
    def Sel_sort(self, arr):
        for i in range(len(arr)-1):
            min_index=i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[min_index]:
                    min_index=j
            arr[i],arr[j]=arr[j],arr[i]
        return arr
obj = Solution()

arr = [5,4,3,2,1]

print(obj.Sel_sort(arr))