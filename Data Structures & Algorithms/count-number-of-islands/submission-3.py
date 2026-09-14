from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_row = len(grid)
        n_col = len(grid[0])
        visited = [[0 for _ in range(n_col)] for _ in range(n_row)]
        n_island = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        def bfs(x,y):
            queue = deque()
            queue.append((x,y))
            visited[x][y] = 1
            while queue:
                x,y = queue.popleft()
                neighbors = []
                for x_del,y_del in directions:
                    if 0<=x+x_del < n_row and 0<=y+y_del < n_col:
                        if grid[x+x_del][y+y_del] =='1':
                            if visited[x+x_del][y+y_del] == 0:
                                queue.append((x+x_del, y+y_del))
                            visited[x+x_del][y+y_del] = 1
        

        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j]=='1' and visited[i][j]==0:
                    bfs(i,j)
                    n_island += 1
        
        return n_island

        