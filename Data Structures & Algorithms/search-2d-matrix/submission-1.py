class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        merged = []

        for i in matrix :
            for j in i : 
                merged.append(j)
        
        l = 0
        r = len(merged)- 1 

        while l<=r :
            mid = (r+l)//2
            if merged[mid] == target :
                return True
            if merged[mid] > target : 
                r = mid - 1 
            else : 
                l = mid + 1 
            
        return False 