#normal
class Solution(object):
    def highestFrequency(self, arr):
        freq = {}

        # Count frequency
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Find highest occurring element
        max_freq = 0
        ans = -1

        for key in freq:
            if freq[key] > max_freq:
                max_freq = freq[key]
                ans = key

        return ans


obj = Solution()
arr = [1, 2, 3, 1, 2, 1, 4, 2, 2]
print(obj.highestFrequency(arr))


#pythonic
class Solution(object):
    def highestFrequency(self, arr):
        freq = {}

        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        max_freq = 0
        ans = -1

        for key, value in freq.items():
            if value > max_freq:
                max_freq = value
                ans = key

        return ans


obj = Solution()
arr = [1, 2, 3, 1, 2, 1, 4, 2, 2]
print(obj.highestFrequency(arr))