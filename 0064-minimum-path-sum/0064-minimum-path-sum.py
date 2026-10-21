class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for _ in range(m)]
       
        def f(i,j):
            
             
            if i>=m or j>=n:
                return float("inf")
            if i==m-1 and j==n-1:
                return grid[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]        
            a=grid[i][j]+f(i+1,j)
            b=grid[i][j]+f(i,j+1)
            dp[i][j]=min(a,b)
            # print(min(a,b))
            return dp[i][j]


            
            
        return f(0,0)

                




        