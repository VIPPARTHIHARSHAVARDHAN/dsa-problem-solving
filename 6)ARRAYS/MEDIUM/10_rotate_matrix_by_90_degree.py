class Solution(object):
    def rotatematrix(self, matrix):
        n = len(matrix)

        ans = [[0] * n for _ in range(n)]   #-> #ans = []

                                                #for i in range(n):
                                                      # row = []
                                                       #for j in range(n):
                                                       # row.append(0)
                                                        #ans.append(row)
                 

        for i in range(n):
            for j in range(n):
                ans[j][n - 1 - i] = matrix[i][j]

        return ans


obj = Solution()

matrix = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [1, 1, 1, 2],
    [3, 5, 7, 8]
]

print(obj.rotatematrix(matrix))


#optimal solution
class Solution(object):

    def rotatematrix(self, matrix):

        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n - 1):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            left = 0
            right = n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = \
                    matrix[i][right], matrix[i][left]

                left += 1
                right -= 1

        return matrix
obj = Solution()

matrix = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [1, 1, 1, 2],
    [3, 5, 7, 8]
]

print(obj.rotatematrix(matrix))