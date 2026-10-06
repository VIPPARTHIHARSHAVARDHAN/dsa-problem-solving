class Solution(object):
    def romanint(self,s):
        values={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res=0
        for i in range(len(s)-1):
            if values[s[i]]<values[s[i+1]]:
                res-=values[s[i]]
            else:
                res+=values[s[i]]
        res+=values[s[-1]]
        return res
obj=Solution()
print(obj.romanint("MCXIV"))


#integer to roman
class Solution(object):
    def intTOrom(self,num):
        values={
            1000:'M',
            900:'CM',
            500:'D',
            400:'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'XL',
            10:'X',
            9:'IX',
            5:"V",
            4:'IV',
            1:'I'
            
            
        }
        res = ""
        for value in values:
            while num>=value:
                res+=values[value]
                num-=value
        return res
        
obj=Solution()
print(obj.intTOrom(58))

        