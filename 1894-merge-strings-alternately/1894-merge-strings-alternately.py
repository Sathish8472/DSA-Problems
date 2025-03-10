class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        i = 0;
        result = ""

        while i < m or i < n:
            if i < m:
                result += word1[i]

            if i < n:
                result += word2[i]
            i += 1
        
        return result
