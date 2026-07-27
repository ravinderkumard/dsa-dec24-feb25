class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])

        def set_value(i,j):
            if i<0 or i>=rows or j<0 or j>=cols or board[i][j]!='O':
                return
            board[i][j] = 'T'
            
            set_value(i+1,j)
            set_value(i-1,j)
            set_value(i,j+1)
            set_value(i,j-1)

        for i in range(rows):
            if board[i][0]=='O':
                set_value(i,0)
            if board[i][cols-1]=='O':
                set_value(i,cols-1)
        
        for i in range(cols):
            if board[0][i]=='O':
                set_value(0,i)
            if board[rows-1][i]=='O':
                set_value(rows-1,i)

        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O':
                    board[i][j] = 'X'
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='T':
                    board[i][j] = 'O'
        