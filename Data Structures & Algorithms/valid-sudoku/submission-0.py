class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = set()
        cols = set()
        boxes = set()

        for r in range(9):
            for c in range(9):

                if board[r][c] == '.':
                    continue
                
                num = board[r][c]
                if (r, num) in rows:
                    return False
                if (c, num) in cols:
                    return False
                if ((r//3, c//3), num) in boxes:
                    return False
                
                rows.add((r, num))
                cols.add((c, num))
                boxes.add(((r//3,c//3),num))

        return True
        