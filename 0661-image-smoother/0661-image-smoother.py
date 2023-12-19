class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        result = [[0] * cols for _ in range(rows)]

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1), (0, 0), (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for i in range(rows):
            for j in range(cols):
                total_sum, count = 0, 0

                for dx, dy in directions:
                    ni, nj = i + dx, j + dy

                    if 0 <= ni < rows and 0 <= nj < cols:
                        total_sum += img[ni][nj]
                        count += 1

                result[i][j] = total_sum // count

        return result