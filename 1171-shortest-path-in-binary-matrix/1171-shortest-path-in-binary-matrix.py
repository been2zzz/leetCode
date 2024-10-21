class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        size = len(grid)
        if grid[0][0] == 1 or grid[size-1][size-1] == 1:
            return -1
        shortest_path = 0
        visited = [[False]*size for _ in range(size)]

        dx = [-1, 1, 0, 0, -1, 1, -1, 1]
        dy = [0 ,0, -1, 1, -1, -1, 1, 1]
        visited[0][0] = True
        queue = deque()
        queue.append((0,0,1))

        while queue:
            cur_x, cur_y, cur_len = queue.popleft()

            if cur_x == size-1 and cur_y == size-1:
                return cur_len 
            for i in range(8):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                if next_x >= 0 and next_x < size and next_y >= 0 and next_y < size and grid[next_x][next_y] == 0 and not visited[next_x][next_y]:
                    visited[next_x][next_y] = True
                    queue.append((next_x, next_y, cur_len + 1))
        return -1

