class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        n = len(isConnected)
        visited = [0] * n

        edges = defaultdict(list)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    edges[i].append(j)

        def bfs(node):
            visited[node] = 1
            q = deque()
            q.append(node)

            while q:
                current_node = q.popleft()

                for neighbor in edges[current_node]:
                    if visited[neighbor] != 1:
                        visited[neighbor] = 1
                        q.append(neighbor)

        def bfs2(node):
            visited[node] = 1
            q = deque()
            q.append(node)

            while q:
                i = q.popleft()

                for neighbor in edges[node]:
                    if visited[neighbor] != 1:
                        visited[neighbor] = 1
                        q.append(neighbor)
            

        def dfs(node):
            visited[node] = 1

            for neighbor in edges[node]:
                if visited[neighbor] != 1:
                    dfs(neighbor)

        for i in range(n):
            if visited[i] != 1:
                bfs(i)
                count += 1

        return count