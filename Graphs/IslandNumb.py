class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or  c >= COLS or grid[r][c] == "0"): # If condition not met, skip
                return
                
            grid[r][c] = "0"            # Replace 1 to 0 so we dont need to pass through again
            for dr, dc in directions:
                dfs(r + dr, c + dc) 

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":   
                    dfs(r, c)
                    islands += 1

        return islands