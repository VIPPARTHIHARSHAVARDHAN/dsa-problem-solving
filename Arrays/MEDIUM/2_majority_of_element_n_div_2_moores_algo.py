#brute force Solution
class Solution(object):
    def majorityelement(self,arr):
        for i in range(len(arr)):
            count=0
            for j in range(len(arr)):
                if arr[j]==arr[i]:
                    count+=1
            if count>len(arr)//2:
                return arr[i]
obj=Solution()
arr=[2,2,3,3,1,2,2]
print(obj.majorityelement(arr))


#better solution
class Solution(object):
    def majorityelement(self, arr):
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        for key, value in freq.items():
            if value > len(arr) // 2:
                return key

#optimal solution when majority is guarantee
class Solution(object):
    def majorityelement(self, arr):
        count = 0
        element = None

        for i in range(len(arr)):
            if count == 0:
                element = arr[i]

            if arr[i] == element:
                count += 1
            else:
                count -= 1

        return element
obj=Solution()
arr=[2,2,3,3,1,2,2]
print(obj.majorityelement(arr))

#optimal solution for majority is not guarantee
class Solution(object):
    def majorityelement(self, arr):
        count = 0
        element = None

        for i in range(len(arr)):
            if count == 0:
                element = arr[i]

            if arr[i] == element:
                count += 1
            else:
                count -= 1
        #check majority
        count=0
        for num in range(len(arr)):
            if arr[num]==element:
                count+=1
        if count>len(arr)//2:
            return element
        else:
            return -1

        
obj=Solution()
arr=[2,2,3,3,1,2,2]
print(obj.majorityelement(arr))