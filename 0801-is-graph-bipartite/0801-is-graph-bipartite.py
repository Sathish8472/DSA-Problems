class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for i in range(n):
            if color[i] == -1:
                #if not self.dfs(i, 0, graph, color):
                if not self.bfs(i, 0, graph, color):
                    return False
        
        return True

    def dfs(self, node: int, col: int,   adj: List[List[int]], color: List[int]) -> bool:
        color[node] = col

        print(node)
        print(adj)

        for neighbor in adj[node]:
            if color[neighbor] == -1:
                if not self.dfs2(neighbor, 1 - col, color, adj):
                    return False
            elif color[neighbor] == col:
                return False
        return True

    def dfs2(self, node, col, color, adj):
        color[node] = col
        
        for neighbor in adj[node]:
            if color[neighbor] == -1:
                if not self.dfs(neighbor, 1 - col, color, adj):
                    return False
            elif color[neighbor] == col:
                return False
        
        return True


    def bfs(self, start, col, graph, color):
        queue = deque()
        queue.append(start)
        color[start] = col

        while queue:
            current = queue.popleft()

            for neighbor in graph[current]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[current]

                    queue.append(neighbor)

                elif color[neighbor] == color[current]:
                    return False
        
        return True