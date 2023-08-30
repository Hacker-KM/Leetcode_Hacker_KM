class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(r, c):
            return 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == '.'
        
        queue = [entrance]
        distance = 0
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                r, c = queue.pop(0)
                if [r, c] != entrance and (r in [0, len(maze) - 1] or c in [0, len(maze[0]) - 1]):
                    return distance
                if r > 0 and valid(r - 1, c):
                    queue.append([r - 1, c])
                    maze[r - 1][c] = '+'
                if r < len(maze) - 1 and valid(r + 1, c):
                    queue.append([r + 1, c])
                    maze[r + 1][c] = '+'
                if c > 0 and valid(r, c - 1):
                    queue.append([r, c - 1])
                    maze[r][c - 1] = '+'
                if c < len(maze[0]) - 1 and valid(r, c + 1):
                    queue.append([r, c + 1])
                    maze[r][c + 1] = '+'
            distance += 1
        
        return -1
