class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return False

        ROWS, COLS = len(board),len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        path = set()

        def depth_first_search(r,c,word_ind):
            if word_ind == len(word):
                return True

            if r <0 or c < 0 or r>= ROWS or c >=COLS or word[word_ind] != board[r][c] or (r,c) in path:
                return False
            
            path.add((r,c))

            res = (depth_first_search(r+1,c,word_ind+1) or
                   depth_first_search(r-1,c,word_ind+1) or
                   depth_first_search(r,c+1,word_ind+1) or
                   depth_first_search(r,c-1,word_ind+1) 
                   )
            path.remove((r,c))            
            return res


        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    result = depth_first_search(i,j,0)
                    if result:
                        return True
        return False