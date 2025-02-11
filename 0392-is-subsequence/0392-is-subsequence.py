class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        index = 0

        if n == 0:
            return True

        for ch in t:
            if index < n and s[index] == ch:
                index += 1

            if index == n:
                return True

        return index == n
