#using built in functions
class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix


# Object creation
obj = Solution()

result = obj.longestCommonPrefix(["flower", "flow", "flight"])

print(result)

#without using built in functions
#using slicing for loop
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        result = ""
        base = strs[0]

        for i in range(0, len(base)):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return result

            result += base[i]

        return result
obj = Solution()

result = obj.longestCommonPrefix(["flower", "flow", "flight"])

print(result)   
#using normal loops
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs)==0:
            return ""
        base=strs[0]
        result=""
        for i in range(len(base)):
            
            for j in range(1,len(strs)):
                word=strs[j]
                if len(word)==i or word[i]!=base[i]:
                    return result
            result+=base[i]
        
obj = Solution()

result = obj.longestCommonPrefix(["flower", "flower", "flight"])

print(result) 

