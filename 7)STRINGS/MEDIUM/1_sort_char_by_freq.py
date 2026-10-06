class Solution(object):
    def fresort(self,s):
        count={}
        for char in s:
            count[char]=count.get(char,0)+1
        bucket={}
        for char,cnt in count.items():
            if cnt not in bucket:
                bucket[cnt]=[]
            bucket[cnt].append(char)
        res=""
        for i in range(len(s),0,-1):
            if i in bucket:
                for c in bucket[i]:
                    res+=c*i
        return res
obj=Solution()
print(obj.fresort("tree"))


#using builtin functions
from collections import Counter,defaultdict
class Solution(object):
    def frequencySort(self, s):
        count=Counter(s)
        buckets=defaultdict(list)
        for char,cnt in count.items():
            buckets[cnt].append(char)
        res=[]
        for i in range(len(s),0,-1):
            if i in buckets:
                for c in buckets[i]:
                    res.append(c*i)
        return "".join(res)
        
        
                    
                