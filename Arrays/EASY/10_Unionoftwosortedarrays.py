class Solution(object):
    def Union(self, arr1, arr2):
        union=set()
        for i in arr1:
            union.add(i)
        for i in arr2:
            union.add(i)
        return sorted(union)
obj=Solution()
arr1=[1,1,2,3,4,4]
arr2=[1,1,2,3,3]
print(obj.Union(arr1,arr2))

#optimal solution
class Solution(object):
    def Union(self, arr1, arr2):
        i = 0
        j = 0
        union = []

        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                if len(union) == 0 or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
            else:
                if len(union) == 0 or union[-1] != arr2[j]:
                    union.append(arr2[j])
                j += 1

        while i < len(arr1):
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1

        while j < len(arr2):
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

        return union


obj = Solution()

arr1 = [1, 1, 2, 3, 4, 4]
arr2 = [1, 1, 2, 3, 3, 5]

print(obj.Union(arr1, arr2))

    