class Solution:

    # time: O(N + M + K logK)
    def mergeSimilarItems(
        self, items1: List[List[int]], items2: List[List[int]]
    ) -> List[List[int]]:

        weight_map = {}

        # time: O(N)
        for value, weight in items1:
            weight_map[value] = weight_map.get(value, 0) + weight

        # time: O(M)
        for value, weight in items2:
            weight_map[value] = weight_map.get(value, 0) + weight
        
        # Sorted: time: O(k log K)
        return sorted([value, weight] for value, weight in weight_map.items())