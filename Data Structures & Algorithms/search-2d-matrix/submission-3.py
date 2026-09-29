class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix)-1, len(matrix[0])-1

        row = float('inf')
        for i in range(m+1):
            if matrix[i][0] == target or matrix[i][n] == target:
                return True
            elif matrix[i][0] < target < matrix[i][n]:
                row = i
                break
        
        if row == float('inf'):
            return False
        
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                left = mid + 1

        return False            
                