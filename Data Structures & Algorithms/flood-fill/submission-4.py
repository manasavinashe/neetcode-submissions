class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]

        if old == color :
            return image 

        def dfs(sr,sc) :
            if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) :
                return 
            if image[sr][sc] != old :
                return 
            image[sr][sc] = color 
            dfs(sr-1, sc) # down
            dfs(sr+1, sc) # up
            dfs(sr, sc-1) # left 
            dfs(sr,sc+1) # right
        
        dfs(sr,sc)
        return image 

        