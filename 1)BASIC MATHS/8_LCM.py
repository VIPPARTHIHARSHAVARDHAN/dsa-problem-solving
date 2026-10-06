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
#without gcd
class Solution(object):

    def lcm(self, a, b):
        max_num = max(a, b)

        while True:
            if max_num % a == 0 and max_num % b == 0:
                return max_num
            max_num += 1


obj = Solution()

a = 12
b = 18

print(obj.lcm(a, b))
                