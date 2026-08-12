class Solution(object):
    def allocatebooks(self, pages, students):
        low = min(pages)
        high = sum(pages)

        while low <= high:
            mid = (low + high) // 2
            current = 0
            no_of_students = 1

            for i in range(len(pages)):
                if current + pages[i] <= mid:
                    current += pages[i]
                else:
                    no_of_students += 1
                    current = pages[i]

            if no_of_students <= students:
                high = mid - 1
            else:
                low = mid + 1

        return low


obj = Solution()
weights = [12,34,67,90]
days = 2

print(obj.allocatebooks(weights, days))