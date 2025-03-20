class Solution:
    def minimumCost(self, n, edges, queries):
        graph =[[] for _ in range(n)]
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        
        visited = [False] * n
        component_id = [-1] * n
        component_min_cost = []

        def bfs(start_node: int, comp_id: int) -> int:
            queue = deque([start_node])
            visited[start_node] = True
            component_id[start_node] = comp_id

            min_and_cost = -1

            while queue:
                node = queue.popleft()
                for neighbor, weight in graph[node]:
                    min_and_cost &= weight
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        component_id[neighbor] = comp_id
                        queue.append(neighbor)
                    
                
            return min_and_cost

        comp_index = 0
        for node in range(n):
            if not visited[node]:
                min_cost = bfs(node, comp_index)
                component_min_cost.append(min_cost)
                comp_index += 1
            
        result = []
        for start, end in queries:
            if component_id[start] == component_id[end]:
                result.append(component_min_cost[component_id[start]])
            else:
                result.append(-1)
            
        return result