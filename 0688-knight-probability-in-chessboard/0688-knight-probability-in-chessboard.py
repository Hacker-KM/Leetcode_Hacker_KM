class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        def checker(x, y):
            return 0 <= x < n and 0 <= y < n

        moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        dp = [[0 for _ in range(n)] for _ in range(n)]

        dp[row][column] = 1


        for m in range(k):

            new_dp = [[0 for _ in range(n)] for _ in range(n)]
            

            for i in range(n):
                for j in range(n):
                    for move_x, move_y in moves:
                        new_x, new_y = i + move_x, j + move_y
                        if checker(new_x, new_y):
                            new_dp[new_x][new_y] += dp[i][j] / 8.0
            

            dp = new_dp


        total_probability = sum(sum(row) for row in dp)

        return total_probability