class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            seen = set()
            for val in board[row]:
                if val == '.':
                    continue
                if val in seen:
                    return False
                seen.add(val)
        
        
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        
        boxes = {}
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == '.':
                    continue
                
                box = (row//3, col//3)
                if box not in boxes:
                    boxes[box] = set()
                if val in boxes[box]:
                    return False

                boxes[box].add(val)

        return True
