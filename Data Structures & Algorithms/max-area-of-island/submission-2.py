class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row,col= len(grid),len(grid[0])
        seen=set()

        def dfs(r,c):
            if r not in range(row) or c not in range(col) or grid[r][c]==0 or (r,c) in seen:
                return 0
            seen.add((r,c))

            return (1+ dfs(1+r,c)+
                       dfs(r-1,c)+
                       dfs(r,1+c)+
                       dfs(r,c-1))
        a=0
        for r in range(row):
            for c in range(col):
                a= max(a,dfs(r,c))
        return a


        
        