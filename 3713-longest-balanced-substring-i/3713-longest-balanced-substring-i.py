class Solution:
    def longestBalanced(self, s: str) -> int:

        max_length = 0
        n = len(s)

        for start in range(n):
            freq = {}
            for end in range(start, n):
                char = s[end]
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
                
                freq_values = list(freq.values())
                if len(set(freq_values)) == 1:
                    max_length = max(max_length, end - start + 1)
        
        return max_length