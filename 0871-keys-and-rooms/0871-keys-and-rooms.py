class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)

        def bfs(v):
            queue = deque()
            queue.append(v)
            visited[v] = True

            while queue:
                cur_room = queue.popleft()
                
                for next_room in rooms[cur_room]:
                    if visited[next_room] == False:
                        visited[next_room] = True
                        queue.append(next_room)
        bfs(0)
        return all(visited)