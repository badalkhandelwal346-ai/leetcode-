class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        island=0
        count=0
        def dfs(i,j,count):
            # nonlocal count
            if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j]!=1:
                return 0
            
            else:
                grid[i][j]=0
                count+=1
                a=dfs(i+1,j,count)
                b=dfs(i,j+1,count)
                c=dfs(i-1,j,count)
                d=dfs(i,j-1,count)
                return 1+a+b+c+d
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    
                    count=dfs(i,j,0)
                    island=max(island,count)
        return island 