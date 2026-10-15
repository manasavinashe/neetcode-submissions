class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        visit = set()
        island = 0
        row, col  = len(grid) , len(grid[0])

        def bfs(r,c) :
            q = collections.deque()
            q.append([r,c])
            visit.add((r,c))
            directions = [[1,0] ,[-1,0] , [0,1], [0,-1]] #down, up, right,left 
            while q :
                r ,c = q.popleft()
                for dr, dc in directions : 
                    row1 = r + dr 
                    col1 = c + dc 
                    if (row1 in range(row) and col1 in range(col)
                    and grid[row1][col1] == '1' and (row1,col1) not in visit) :
                        q.append([row1,col1])
                        visit.add((row1,col1))
        for r in range(row):
            for c in range(col) : 
                if grid[r][c] == "1" and (r,c) not in visit :
                    bfs(r,c)
                    island +=1
        return island