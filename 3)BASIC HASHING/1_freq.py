class Solution(object):
    def frequencyCount(self, arr):
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        return freq


obj = Solution()
arr = [1, 2, 1, 3, 2, 1, 4]
print(obj.frequencyCount(arr))


#char hashing using hashmap
class Solution(object):
    def characterHashing(self, s):
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        return freq


obj = Solution()
s = "abacaba"
print(obj.characterHashing(s))



#we can also use array list if once refer chatgpt