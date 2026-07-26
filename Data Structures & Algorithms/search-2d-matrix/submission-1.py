class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        right = (len(matrix[0]) * len(matrix))-1
        left = 0
        while left <= right:
            m = left + ((right-left)//2)
            row = m // len(matrix[0])
            cols = m % len(matrix[0])
            if matrix[row][cols] > target:
                right = m - 1
            elif matrix[row][cols] < target:
                left = m + 1
            elif matrix[row][cols] == target:
                return True
        return False
