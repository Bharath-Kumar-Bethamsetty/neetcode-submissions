class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        m, n = len(matrix), len(matrix[0])

        for r in range(m):
            for c in range(r,n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
        for row in matrix:
            row.reverse()

