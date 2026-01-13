class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            board_row = board[row]
            board_row = [t for t in board_row if t != '.']
            if len(board_row) != len(set(board_row)):
                return False
        for col in range(9):
            board_col = [board[row][col] for row in range(9)]
            board_col = [t for t in board_col if t != '.']
            if len(board_col) != len(set(board_col)):
                return False
        for x in [0, 3, 6]:
            for y in [0, 3, 6]:
                cell = [board[x+i][y+j] for i in range(3) for j in range(3)]
                cell = [t for t in cell if t != '.']
                if len(cell) != len(set(cell)):
                    return False
        return True
