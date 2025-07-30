class Solution:
    def topKFrequent1(self, words: List[str], k: int) -> List[str]:
        
        freq = Counter(words)

        max_heap = [(-count, word) for word, count in freq.items()]
        
        heapq.heapify(max_heap)

        result = []
        while k > 0:
            count, word = heapq.heappop(max_heap)
            result.append(word)
            k -= 1


        return result
    
    # time: O(n + k log n), space: O(N)
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)

        heap = [(-count, word) for word, count in freq.items()]
        heapq.heapify(heap)     # O(N)

        result = []
        
        for _ in range(k):          # O(k log N)
            count, word = heapq.heappop(heap)   
            result.append(word)

        return result