class Solution:
    def numberOfPaths2(self, n: int, corridors: List[List[int]]) -> int:
        count = 0
        adj = {i + 1: set() for i in range(n)}

        for u, v in corridors:
            adj[u].add(v)
            adj[v].add(u)

        print("adj: ", adj)
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                for k in range(j + 1, n + 1):
                    if j in adj[i] and k in adj[j] and i in adj[k]:
                        count += 1

        return count
        
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        count = 0
        adj = {i + 1: set() for i in range(n)}

        for u, v in corridors:
            adj[u].add(v)
            adj[v].add(u)

        for i in range(1, n + 1):
            neighbors_i = adj[i]
            for j in neighbors_i:
                if j > i:  # Consider each undirected edge only once
                    common_neighbors = neighbors_i.intersection(adj[j])
                    for k in common_neighbors:
                        if k > j:  # Enforce an order to count each cycle once
                            count += 1

        return count
