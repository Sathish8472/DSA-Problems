class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return

            for end in range(start, len(s)):
                substring = s[start : end + 1]
                if isPalindrome(substring):
                    path.append(substring)
                    backtrack(end + 1, path)
                    path.pop()

        def isPalindrome(substring):
            return substring == substring[::-1]

        backtrack(0, [])
        return result
