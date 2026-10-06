class Solution(object):

    def beauty(self, s):
        result=0
        for i in range(len(s)):
            freq={}
            for j in range(i,len(s)):
                freq[s[j]]=freq.get(s[j],0)+1
                maximum=0
                minimum=0
                for ele,count in freq.items():
                    if count>maximum:
                        maximum=max(count,maximum)
                    if count>minimum:
                        minimum=1
                beauty=maximum-minimum
            result+=beauty
        return result               
obj=Solution()
print(obj.beauty("abaacc"))