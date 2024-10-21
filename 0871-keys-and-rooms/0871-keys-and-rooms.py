class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)

        def dfs(v):
            visited[v] = True
            for next_room in rooms[v]:
                if visited[next_room] == False:
                    dfs(next_room)
        dfs(0)
        return all(visited)