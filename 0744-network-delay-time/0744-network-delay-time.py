class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))
        
        print("graph: ", graph)

        dist = {i: float('inf') for i in range(1, n + 1)}

        dist[k] = 0
        print("dist: ", dist)

        pq = [(0, k)]

        while pq: 
            current_time, current_node = heapq.heappop(pq)

            if current_time > dist[current_node]:
                continue
            
            for neighbor, weight in graph[current_node]:
                time_to_neighbor = current_time + weight
                if time_to_neighbor < dist[neighbor]:
                    dist[neighbor] = time_to_neighbor
                    heapq.heappush(pq, (time_to_neighbor, neighbor))
                
        max_delay = 0
        print("dist: ", dist)
        for node_dist in dist.values():
            if node_dist == float('inf'):
                return -1
            max_delay = max(max_delay, node_dist)
        
        return max_delay