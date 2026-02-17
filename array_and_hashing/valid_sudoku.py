from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rs = set()
        cs = set()
        ss = set()
        i = 0
        is_valid_sudoku = True

        while i < 9 and is_valid_sudoku:
            j = 0
            while j < 9 and is_valid_sudoku:
                n = board[i][j]
                if n != '.':
                    # Usamos el índice único de subcuadro: (i // 3) * 3 + (j // 3)
                    square_idx = (i // 3) * 3 + (j // 3)
                    if (i, n) in rs or (j, n) in cs or (square_idx, n) in ss:
                        is_valid_sudoku = False
                    else:
                        rs.add((i, n))
                        cs.add((j, n))
                        ss.add((square_idx, n))
                j += 1
            i += 1

        return is_valid_sudoku