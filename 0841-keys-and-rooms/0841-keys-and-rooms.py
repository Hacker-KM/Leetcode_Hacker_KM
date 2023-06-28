class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # l = []
        # for i in range(0,len(rooms)):
        #     if i+1 not in rooms[i] and rooms[i]!=[]:
        #         return False
        #     else:
        #         l.append((i+1)
        # return True
        visited = set()
        def helper(room):
            if room in visited:
                return 
            visited.add(room)
            for other in rooms[room]:
                helper(other)
        helper(0)
        return len(visited) == len(rooms)
