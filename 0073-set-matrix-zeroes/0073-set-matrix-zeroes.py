class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    for k in range(len(matrix[i])):
                        if matrix[i][k] != 0:
                            matrix[i][k]=float('inf')
                    for t in range(len(matrix)):
                        if matrix[t][j] != 0:
                            matrix[t][j]=float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==float('inf'):
                    matrix[i][j]=0
        
        return matrix