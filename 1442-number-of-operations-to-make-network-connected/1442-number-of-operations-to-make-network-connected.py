class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
    
    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

class Solution:
    # Using DFS/BFS
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        adj = [[] for _ in range(n)]

        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        numberOfConnectedComponents = 0
        visited = [False for _ in range(n)]

        def dfs(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        def bfs(node):
            queue = deque()
            queue.append(node)

            while queue:
                curr = queue.popleft()
                visited[curr] = True

                for neighbor in adjNode[curr]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
                

        for i in range(n):
            if not visited[i]:
                numberOfConnectedComponents += 1
                # dfs(i)
                dfs(i)
        
        return numberOfConnectedComponents - 1



    # Using Disjoint Set

    def makeConnected1(self, n: int, connections: List[List[int]]) -> int:
        size = len(connections)

        if size < n - 1:
            return -1
        
        ds = DisjointSet(n)

        for i in range(size):
            ds.unionByRank(connections[i][0], connections[i][1])
        
        count = 0

        for i in range(n):
            if ds.parent[i] == i:
                count += 1
            
        return count - 1