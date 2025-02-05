class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def bfs(x, y):
            dx = [-1, 1, 0, 0]
            dy = [0 ,0, -1, 1]
            visited[x][y] = True
            queue = deque()
            queue.append((x,y))
            while queue:
                cur_x, cur_y = queue.popleft()
                for i in range(4):
                    next_x = cur_x + dx[i]
                    next_y = cur_y + dy[i]
                    if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n and grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))


        for i in range(m):          
            for j in range(n):   
                if grid[i][j] == '1' and visited[i][j] == False:
                    bfs(i, j)
                    island_count += 1
        return island_count
