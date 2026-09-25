class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)*len(matrix[0]) - 1 
        n = len(matrix[0])
        while l <=r : 
            mid = (r+l)//2
            val = matrix[mid//n][mid%n]

            if val == target :
                return True
            elif val > target :
                r = mid -1 
            else : 
                l = mid + 1 
        return False
