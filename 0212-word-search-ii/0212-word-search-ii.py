class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Step 1: Build Trie
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = word   # '#' marks end of word
        
        m, n = len(board), len(board[0])
        result = []

        def dfs(i, j, node):
            char = board[i][j]
            if char not in node:
                return
            next_node = node[char]
            
            if '#' in next_node:  # Found a word
                result.append(next_node['#'])
                del next_node['#']  # avoid duplicates
            
            board[i][j] = "#"  # mark visited
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni, nj = i+dx, j+dy
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != "#":
                    dfs(ni, nj, next_node)
            board[i][j] = char  # backtrack

            if not next_node:  # prune Trie
                node.pop(char)

        # Step 2: Start DFS from every cell
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)

        return result


    def findWords1(self, board: List[List[str]], words: List[str]) -> List[str]:
        row_len, col_len = len(board), len(board[0])
        result = []
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def dfs(row, col, ind, word, visited):
            if ind == len(word):
                return True

            visited[row][col] = True

            for dx, dy in directions:
                nr, nc = row + dx, col + dy
                if 0 <= nr < row_len and 0 <= nc < col_len:
                    if not visited[nr][nc] and board[nr][nc] == word[ind]:
                        if dfs(nr, nc, ind + 1, word, visited):
                            return True

            visited[row][col] = False
            return False

        for word in words:
            found = False
            for i in range(row_len):
                for j in range(col_len):
                    if board[i][j] == word[0]:
                        visited = [[False] * col_len for _ in range(row_len)]
                        if dfs(i, j, 1, word, visited):
                            result.append(word)
                            found = True
                            break  # break inner loop
                if found:
                    break  # break outer loop

        return result
