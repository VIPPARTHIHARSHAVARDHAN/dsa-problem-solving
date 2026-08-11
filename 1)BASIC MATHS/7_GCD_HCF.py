class Solution(object):
    def gcd(self, n1,n2):
        gcd=1
        for i in range(1,min(n1,n2)+1):
            if n1%i==0 and n2%i==0:
                gcd=i
        return gcd
obj=Solution()
print(obj.gcd(9,12))

#gcd using euclidean algo
class Solution(object):
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

obj = Solution()

print(obj.gcd(48, 36))  # 12
print(obj.gcd(36, 48))  # 12

                