#using counter
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)



class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        
        countS,countT={},{}
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        for c in countS:
            if countS[c]!=countT.get(c,0):
                return False
        return True
obj = Solution()

# Method call
result = obj.isAnagram("anagram", "nagaram")

print(result)