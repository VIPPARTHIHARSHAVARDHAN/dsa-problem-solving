class Solution(object):
    def LCM(self, n1,n2):
        gcd=1
        for i in range(1,min(n1,n2)+1):
            if n1%i==0 and n2%i==0:
                gcd=i
        Lcm=(n1*n2)//gcd
        return Lcm
obj=Solution()
print(obj.LCM(9,12))
                