class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return None
        row, col= len(grid), len(grid[0])
        seen= set()
        island=0
        

        def dfs(r,c):
            if r not in range(row) or c not in range(col) or (r,c) in seen or grid[r][c]=="0":
                return


            directions= [[1,0],[-1,0],[0,1],[0,-1]]

            for dr,dc in directions:
                rows,cols= r+dr , c+dc
                dfs(rows,cols)
                seen.add((r,c))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r,c) not in seen:
                    dfs(r,c)
                    island+=1
        return island
        