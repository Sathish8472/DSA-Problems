# DFS - Brute force
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def has_cycle(src, dest, visited):
            if src == dest:
                return True

            visited.add(src)
            for neighbor in graph[src]:
                if neighbor not in visited:
                    if has_cycle(neighbor, dest, visited):
                        return True
            return False

        for u, v in edges:
            if u in graph and v in graph and has_cycle(u, v, set()):
                return [u, v]

            graph[u].append(v)
            graph[v].append(u)

        return []
