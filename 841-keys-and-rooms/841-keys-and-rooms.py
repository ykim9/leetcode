class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()
        def dfs(room):
            if room not in visited:
                visited.add(room)
                for x in rooms[room]:
                    dfs(x)
        dfs(0)
        return len(visited) == n