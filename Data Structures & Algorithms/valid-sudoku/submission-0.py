class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = set()
        column_set = set()
        box_set = set()
        for row in range(len(board)):
            for i in range(len(board[row])):
                box_id = (row // 3) * 3 + (i // 3)
                if board[row][i] != ".":
                    if f'{board[row][i]} in row {row}' in row_set:
                        return False
                    row_set.add(f'{board[row][i]} in row {row}')
                    if f'{board[row][i]} in column {i}' in column_set:
                        return False
                    column_set.add(f'{board[row][i]} in column {i}')
                    if f'{board[row][i]} in box {box_id}' in box_set:
                        return False
                    box_set.add(f'{board[row][i]} in box {box_id}')
        return True