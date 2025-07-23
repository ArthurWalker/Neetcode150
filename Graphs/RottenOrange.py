class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # q = collections.deque()
        # fresh = 0
        # time = 0

        # for r in range(len(grid)):
        #     for c in range(len(grid[0])):
        #         if grid[r][c] == 1:
        #             fresh += 1
        #         if grid[r][c] == 2:
        #             q.append((r, c))

        # directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # while fresh > 0 and q:
        #     length = len(q)
        #     for i in range(length):
        #         r, c = q.popleft()

        #         for dr, dc in directions:
        #             row, col = r + dr, c + dc
        #             if (row in range(len(grid))
        #                 and col in range(len(grid[0]))
        #                 and grid[row][col] == 1
        #             ):
        #                 grid[row][col] = 2
        #                 q.append((row, col))
        #                 fresh -= 1
        #     time += 1
        # return time if fresh == 0 else -1

        ROWS, COLS = len(grid),len(grid[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        initial_rotton = []  
        visited = []
        fresh_numb = 0
        # Look for rotten fruit to set as the root nodes and count fresh 
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    initial_rotton.append((row,col))
                    visited.append((row,col))
                elif grid[row][col] == 1:
                    fresh_numb+=1
        rot_numb = len(initial_rotton)

        if rot_numb == fresh_numb == 0:
            return 0
        if rot_numb == 0:
            return -1
        queue = initial_rotton
        level = 0    # can be understood as minute
        fresh_to_rot = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                row,col = queue.pop(0)
                # Travesal
                for dr, dc in directions:
                    new_r, new_c = dr+row, dc+col
                    if grid[row][col] == 2 and 0 <= new_r < ROWS and 0 <= new_c < COLS and grid[new_r][new_c] == 1 and grid[new_r][new_c] not in visited:
                        queue.append((new_r,new_c))
                        visited.append((new_r,new_c))
                        grid[new_r][new_c] = 2
                        fresh_to_rot+=1

            level+=1
        print(fresh_numb,fresh_to_rot,level-1)
        
        fresh_left =  fresh_numb - fresh_to_rot
        if fresh_left != 0:
            return -1
        
        return level-1