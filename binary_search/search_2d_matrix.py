class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        row,col = len(matrix),len(matrix[0])
        left,right = 0, row*col - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // col
            Col = mid % col
            current_val = matrix[row][Col]

            if current_val == target:
                return True
            elif current_val > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False