class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid) # no of rows
        n = len(grid[0]) # no of columns 
        fresh = 0
        q = deque()
        for i in range(m) :
            for j in range(n) :
                a = grid[i][j]
                if a == 2 :
                    q.append([i,j])
                elif a == 1 :
                    fresh +=1 
        timer = 0 
        while q and fresh > 0 :
            for i in range(len(q)):
                r, c = q.popleft()
                for x, y in ((-1,0), (1,0), (0,1), (0,-1)):
                    if r+y < 0 or r+y >= m or c+x < 0 or c+x >= n:
                        continue
                    elif grid[r+y][c+x] == 1:
                        grid[r+y][c+x] = 2   # mark at enqueue time
                        fresh -= 1
                        q.append([r+y, c+x])
            timer += 1
        return timer if fresh == 0 else -1

                    





        