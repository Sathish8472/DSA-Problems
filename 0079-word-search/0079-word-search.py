class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len, col_len = len(board), len(board[0])

        visited = [[False] * col_len for _ in range(row_len)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col, ind):
            if ind == len(word):
                return True

            visited[row][col] = True

            for dx, dy in directions:
                nr, nc = row + dx, col + dy
                if 0 <= nr < row_len and 0 <= nc < col_len:
                    if not visited[nr][nc] and board[nr][nc] == word[ind]:
                        if dfs(nr, nc, ind + 1):
                            return True

            visited[row][col] = False
            return False

        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True

        return False