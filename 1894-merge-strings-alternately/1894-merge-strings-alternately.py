class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_len = max(len(word1), len(word2))
        i = 0;
        result = ""

        while i < max_len:
            if i < len(word1):
                result += word1[i]

            if i < len(word2):
                result += word2[i]
            i += 1
        
        return result
