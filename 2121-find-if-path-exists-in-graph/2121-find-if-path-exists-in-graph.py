class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])

        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)

        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1   

class Solution:
    # Disjoint solution: Optimized solution
    def validPath_1(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        ds = DisjointSet(n)

        for u, v in edges:
            ds.union(u, v)

        return ds.find(source) == ds.find(destination)



    # DFS & BFS approach
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        """Build adjacency list"""
        graph= {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
       
        # BFS
        def bfs(source):
            queue = deque([source])
            visited = set([source])

            while queue:
                node = queue.popleft()
                if node == destination:
                    return True
                
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return False

        # DFS approach
        def dfs(node):
            
            if node == destination:
                return True
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True

            return False
        
        return bfs(source)

        
