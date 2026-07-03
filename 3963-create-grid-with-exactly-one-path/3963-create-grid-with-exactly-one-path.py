class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        matrix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==n-1:
                    matrix[i][j]="."
                else:
                    matrix[i][j]="#"
        return ["".join(row) for row in matrix]



        
        
        