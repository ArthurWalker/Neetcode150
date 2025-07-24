class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board),len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        regions_0 = []

        def bfs(row,col):
            queue = [(row,col)]
            visitted = [(row,col)]

            while queue:
                level_size = len(queue)
                for _ in range(level_size):
                    temp_r,temp_c = queue.pop(0)
                    
                    for dr,dc in directions:
                        new_r, new_c = dr+temp_r, dc+temp_c
                        if 0 <= new_r < ROWS and 0 <= new_c < COLS and board[new_r][new_c] == 'O' and (new_r,new_c) not in visitted:
                            queue.append((new_r,new_c))
                            visitted.append((new_r,new_c))
            regions_0.append(visitted)

        def check_exist(row,col,regions):
            flattened = [item for row in regions for item in row]
            if (row,col) in flattened:
                return True
            return False

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == 'O' and not check_exist(row,col,regions_0) :
                    bfs(row,col)  # Find all regions
        
        # Check valid region

        for region in regions_0[:]:
            for cell in region:
                if cell[0] == ROWS-1 or cell[0] == 0 or cell[1] == COLS-1 or cell[1]==0:
                    regions_0.remove(region)
                    break
        
        for i,v in enumerate(regions_0):
            for cell in v:
                r,c = cell[0],cell[1]
                board[r][c] = 'X'
            


