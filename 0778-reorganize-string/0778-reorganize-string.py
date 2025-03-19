class Solution:
    def reorganizeString(self, s: str) -> str:

        count = Counter(s)
        print(count)

        max_heap = [(-freq, char) for char, freq in count.items()]
        print(max_heap)

        heapq.heapify(max_heap)
        
        if any(-freq > (len(s) + 1) // 2 for freq, char in max_heap):
            return ""
        
        result = []
        prev_freq, prev_char = 0, ""

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            
            prev_freq, prev_char = freq + 1, char
            
        return "".join(result)