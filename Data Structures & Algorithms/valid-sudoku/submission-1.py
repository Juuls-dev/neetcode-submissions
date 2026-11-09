class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for i in range(9):
                if board[r][i] == '.':
                    continue
                elif board[r][i] in seen :
                    return False
                else:
                    seen.add(board[r][i])
        for c in range(9):
            seen = set()
            for i in range(9):
                if board[i][c] == '.':
                    continue
                elif board[i][c] in seen :
                    return False
                else:
                    seen.add(board[i][c])
        for sq in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (sq // 3) * 3 + i
                    c = (sq % 3) * 3 + j
                    if board[r][c] == '.':
                        continue
                    elif board[r][c] in seen :
                        return False
                    else:
                        seen.add(board[r][c])
        return True