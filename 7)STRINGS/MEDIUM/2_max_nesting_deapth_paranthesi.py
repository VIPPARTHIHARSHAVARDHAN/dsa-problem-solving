class Solution(object):
    def maxnesting(self,s):
        res=0
        cur=0
        for c in s:
            if c=="(":
                cur+=1
            elif c==")":
                cur-=1
            res=max(cur,res)
        return res
obj=Solution()
print(obj.maxnesting("((()))"))