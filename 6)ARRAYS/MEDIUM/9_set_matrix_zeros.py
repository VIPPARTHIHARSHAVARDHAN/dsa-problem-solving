class Solution(object):
    def setZeroes(self, matrix):
        rows=len(matrix)
        col=len(matrix[0])
        for i in range(rows):
            for j in range(col):
                if matrix[i][j]==0:
                    #make entire row to -1
                    for k in range(col):
                        if matrix[i][k]!=0:
                            
                            matrix[i][k]=-1
                        # Mark the entire column
                    for k in range(rows):
                        if matrix[k][j] != 0:
                            matrix[k][j] = -1
        
        for i in range(rows):
            for j in range(col):
                if matrix[i][j]==-1: 
                    matrix[i][j]=0
        return matrix
obj = Solution()
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print(obj.setZeroes(matrix))


#optimal solution
class Solution(object):
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        col0 = 1
        for i in range(n):
            if matrix[i][0] == 0:
                col0 = 0

            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, 0, -1):

                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

            # Handle first column separately
            if col0 == 0:
                matrix[i][0] = 0

        return matrix
obj = Solution()

matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print(obj.setZeroes(matrix))

                              
                