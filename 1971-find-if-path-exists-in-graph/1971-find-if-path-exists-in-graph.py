class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        new=[False]*n
        adjlist=[[] for _ in range(n)]
        for u,v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)
        def dfs(i):
            new[i]=True
            for j in range(len(adjlist[i])):
                if new[adjlist[i][j]]==False:
                    dfs(adjlist[i][j])
                   


        
        dfs(source)
        if new[destination]:
            return True
        else:
            return False