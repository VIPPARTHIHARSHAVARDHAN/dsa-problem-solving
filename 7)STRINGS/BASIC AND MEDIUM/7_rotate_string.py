class Solution(object):
    def rotate(self,s,goal):
        if len(s)!=len(goal):
            return False
        return goal in s+s
obj = Solution()
result = obj.rotate("abcde", "cdeab")
print(result)
    
#without in
class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        n = len(s)

        for start in range(n):
            match = True

            for i in range(n):
                if s[(start + i) % n] != goal[i]:
                    match = False
                    break

            if match:
                return True

        return False
obj = Solution()

result = obj.rotateString("abcde", "cdeab")

print(result)
        