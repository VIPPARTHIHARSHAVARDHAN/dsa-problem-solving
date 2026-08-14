#without using inbuilt
class Solution:
    def largestOddNumber(self, num):
        #len
        n = 0

        for ch in num:
            n += 1

        i = n - 1

        while i >= 0:
            digit = ord(num[i]) - ord('0')

            if digit % 2 != 0:
                ans = ""
                j = 0

                while j <= i:
                    ans += num[j]
                    j += 1

                return ans

            i -= 1

        return ""
obj = Solution()

# Calling the method
result = obj.largestOddNumber("35426")

print(result)
    
    #without using slicing
class Solution:
    def largestOddNumber(self, num):
        n=len(num)-1
        while n>=0:
            if int(num[n])%2!=0:
                ans=""
                for j in range(n+1):
                    ans+=num[j]
                return ans
            n-=1
        return ""
obj = Solution()

# Calling the method
result = obj.largestOddNumber("35426")

print(result)
                
                
#with built in functions  
class Solution:
    def largestOddNumber(self, num):
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]

        return ""


# Object creation
obj = Solution()

# Method call
result = obj.largestOddNumber("35426")

print(result)  
            
    
