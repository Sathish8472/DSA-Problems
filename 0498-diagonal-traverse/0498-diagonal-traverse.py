class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        direction = 1  # 1 = up-right, -1 = down-left
        for _ in range(m * n):
            result.append(mat[row][col])
            if direction == 1:
                if col == n - 1:
                    row += 1
                    direction = -1
                elif row == 0:
                    col += 1
                    direction = -1
                else:
                    row -= 1
                    col += 1
            else:
                if row == m - 1:
                    col += 1
                    direction = 1
                elif col == 0:
                    row += 1
                    direction = 1
                else:
                    row += 1
                    col -= 1

        return result

    def findDiagonalOrder1(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        diagonals = {}

        for i in range(m):
            for j in range(n):
                d = i + j
                if d not in diagonals:
                    diagonals[d] = []
                diagonals[d].append(mat[i][j])

        print(diagonals)
        result = []
        for d in range(m + n - 1):
            if d % 2 == 0:
                result.extend(reversed(diagonals[d]))
            else:
                result.extend(diagonals[d])

        return result
