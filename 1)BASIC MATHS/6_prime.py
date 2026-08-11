class Solution(object):
    def isPrime(self, n):
        if n <= 1:
            return False

        for i in range(2, n):
            if n % i == 0:
                return False

        return True


obj = Solution()

n = int(input("Enter a number: "))

if obj.isPrime(n)==True:
    print("Prime")
else:
    print("Not Prime")
    