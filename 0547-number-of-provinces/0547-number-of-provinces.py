class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        n = len(isConnected)
        visited = [0] * n
        edges = defaultdict(list)

        # Adjacency Matrix representation
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    edges[i].append(j)

        # Adjacency Lists
        # for u, v in edges:
        #     graph[u].append(v)
        #     graph[v].append(u)
        print(edges)
        for i in range(n):
            if visited[i] != 1:
                self.dfs(i, visited, edges)
                count += 1

        return count
    
    def bfs(self, root, visited, edges):
        q = deque([root])
        visited[root] = 1

        while q:
            current_node = q.popleft()

            for neighbor in edges[current_node]:
                if visited[neighbor] != 1:
                    q.append(neighbor)
                    visited[neighbor] = 1

    def dfs(self, node, visited, edges):
        visited[node] = 1

        for neighbor in edges[node]:
            if visited[neighbor] != 1:
                self.dfs(neighbor, visited, edges)