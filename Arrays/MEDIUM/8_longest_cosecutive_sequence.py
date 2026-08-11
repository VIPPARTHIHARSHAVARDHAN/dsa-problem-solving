#brute force solution
class Solution(object):
    def conseq(self,arr):
        longest=1
        count=1
        arr.sort()
        for i in range(1,len(arr)):
            if arr[i]==arr[i-1]:
                continue
            elif arr[i]==arr[i-1]+1:
                count+=1
                longest=max(count,longest)
            else:
                
                count=1
        return longest

obj = Solution()
arr = [100, 4, 200, 1, 3, 2]
print(obj.conseq(arr))

#another approach of brute force
class Solution(object):
    def conseq(self, arr):
        if not arr:
            return 0

        longest = 0

        for i in range(len(arr)):
            num = arr[i]

            if num - 1 not in arr:
                count = 1
                current = num

                while current + 1 in arr:
                    current += 1
                    count += 1

                if count > longest:
                    longest = count

        return longest

obj = Solution()
arr = [100, 4, 200, 1, 3, 2]
print(obj.conseq(arr))

#optimal solution
class Solution(object):
    def conseq(self, arr):
        if not arr:
            return 0
        s=set(arr)
        longest=0
        for num in s:
            if num-1 not in s:
                count=1
                x=num
                while x+1 in s:
                    x+=1
                    count+=1
                longest=max(longest,count)
        return longest
obj = Solution()
arr = [100, 4, 200, 1, 3, 2]
print(obj.conseq(arr))
            
        