class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        m, n = len(board), len(board[0])

        # Rows
        for r in range(m):
            seen = set()
            for c in range(n):
                if board[r][c] == '.':
                    continue

                if board[r][c] in seen:
                    return False

                seen.add(board[r][c])

        # Columns
        for c in range(n):
            seen = set()
            for r in range(m):
                if board[r][c] == '.':
                    continue

                if board[r][c] in seen:
                    return False

                seen.add(board[r][c])

        # Boxes
        boxes = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                box = (r // 3, c // 3)

                if box not in boxes:
                    boxes[box] = set()

                if board[r][c] in boxes[box]:
                    return False

                boxes[box].add(board[r][c])

        return True