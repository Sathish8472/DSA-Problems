class Solution:

    def build_graph(self, edges, num_nodes):
        graph = {i : [] for i in range(num_nodes)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        return graph

    def get_bob_path(self, graph, bob: int, num_nodes: int):
        bob_path_time = [-1] * num_nodes
        path_trace = []

        def dfs_bob(node, parent):
            if node == 0:
                return True
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    path_trace.append(node)
                    if dfs_bob(neighbor, node):
                        return True
                    path_trace.pop()
                
        dfs_bob(bob, -1)

        for timestamp, node in enumerate(path_trace):
            bob_path_time[node] = timestamp
        
        return bob_path_time
    
    def get_max_profit(self, graph, amount, bob_path_time):
        
        def dfs_alice(node, parent, curr_profit, time_elapsed):
            if bob_path_time[node] == -1 or bob_path_time[node] > time_elapsed:
                curr_profit += amount[node]
            elif bob_path_time[node] == time_elapsed:
                curr_profit += amount[node] // 2
            
            if len(graph[node]) == 1 and node != 0:
                return curr_profit
            
            max_profit = float('-inf')
            for neighbor in graph[node]:
                if neighbor != parent:
                    max_profit = max(max_profit, dfs_alice(neighbor, node, curr_profit, time_elapsed + 1))
                
            return max_profit
        
        return dfs_alice(0, -1, 0, 0)

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        num_nodes = len(amount)
        graph = self.build_graph(edges, num_nodes)
        bob_path_time = self.get_bob_path(graph, bob, num_nodes)
        return self.get_max_profit(graph, amount, bob_path_time)
        