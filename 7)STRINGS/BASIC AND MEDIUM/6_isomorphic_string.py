class Solution:
    def iso(self, s,t):
        mapST,mapTS={},{}
        for i in range(len(s)):
            c1,c2=s[i],t[i]
            if ((c1 in mapST and mapST[c1]!=c2) or
                (c2 in mapTS and mapTS[c2]!=c1)):
                    return False
            mapST[c1]=c2
            mapTS[c2]=c1
        return True
                
        
        
obj = Solution()
s="add"
t="egg"
result = obj.iso(s,t)

print(result) 