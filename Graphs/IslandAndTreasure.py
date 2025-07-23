class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        visisted = set()
        INF = 2147483647
        # def dfs(row,col):
        #     if row >= ROWS or col >= COLS or row < 0 or col < 0 or grid[row][col] == -1 or  (row,col) in visisted:
        #         return INF
            
        #     if grid[row][col] == 0:
        #         return 0

        #     visisted.add((row,col))

        #     val = INF                            # Set the max of the current travel so we can bypass
        #     for dr, dc in directions:
        #         val = min(val,1+dfs(row+dr,col+dc))     # Since only the right travel to 0 is normal number, it is easy to compare between normal number and INF

        #     visisted.remove((row,col))                  # Remove so the next node can be visisted from other node
        #     return val

        def bfs(row,col):
            queue = [(row,col)]
            visisted = set()
            visisted.add((row,col))
            steps = 0
            while queue:
                for _ in range(len(queue)):
                    row,col = queue.pop(0)
                    if grid[row][col] == 0:
                        return steps
                    for dr,dc in directions:
                        new_r,new_c = row+dr,col+dc
                        if 0 <= new_r < ROWS and 0<=new_c<COLS and (new_r,new_c) not in visisted and grid[new_r][new_c] != -1:
                            visisted.add((new_r,new_c))
                            queue.append((new_r,new_c))
                steps+=1
            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r,c)