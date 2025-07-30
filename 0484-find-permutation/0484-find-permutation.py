class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s) + 1
        result = list(range(1, n + 1))
        i = 0

        while i < len(s):
            if s[i] == 'D':
                start = i
                while i < len(s) and s[i] == 'D':
                    i += 1
                result[start: i + 1] = reversed(result[start:i+1])
            else:
                i += 1

        return result
        