class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS, COLS = len(grid),len(grid[0])
        island = 0
        island_lst = {}
        visisted = []

        def dfs(r,c):
            if r >= ROWS or r < 0 or c < 0 or c >= COLS or grid[r][c]==0:
                return
            if island not in island_lst:
                island_lst[island]=1
            else:
                island_lst[island]+=1
            grid[r][c] = 0
            for dr, dc in directions:
                dfs(r+dr,c+dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    island+=1
                    dfs(r,c)
        if len(island_lst) == 0:
            return 0
        return max(island_lst.values())