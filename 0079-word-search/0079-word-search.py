class Solution:
    def exist1(self, board: List[List[str]], word: str) -> bool:
        row_len, col_len = len(board), len(board[0])

        visited = [[0] * col_len for _ in range(row_len)]
        print(visited)

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col, ind):
            if ind == len(word):
                return True

            visited[row][col] = 1

            for dx, dy in directions:
                nr = row + dx
                nc = col + dy
                if 0 <= nr < row_len and 0 <= nc < col_len:
                    print(nr, nc, ind)
                    if visited[nr][nc] != 1 and board[nr][nc] == word[ind]:
                        if dfs(nr, nc, ind + 1):
                            return True

            visited[row][col] = 0
            board[row][col] = tem
            return False

        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len, col_len = len(board), len(board[0])

        # Early pruning: check if board has enough characters
        board_counter = Counter(char for row in board for char in row)
        word_counter = Counter(word)
        for char in word_counter:
            if word_counter[char] > board_counter.get(char, 0):
                return False

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        visited = [[False] * col_len for _ in range(row_len)]

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

            visited[row][col] = False  # backtrack
            return False

        for i in range(row_len):
            for j in range(col_len):
                if board[i][j] == word[0]:
                    if dfs(i, j, 1):
                        return True

        return False
