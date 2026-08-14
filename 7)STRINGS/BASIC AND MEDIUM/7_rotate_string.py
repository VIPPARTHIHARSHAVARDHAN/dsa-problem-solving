class Solution(object):
    def rotate(self,s,goal):
        if len(s)!=len(goal):
            return False
        return goal in s+s
obj = Solution()
result = obj.rotate("abcde", "cdeab")
print(result)
    
        