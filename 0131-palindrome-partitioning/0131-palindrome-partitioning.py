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
                    backtrack(end + 1, path + [substring])

        def isPalindrome(substring):
            return substring == substring[::-1]

        backtrack(0, [])
        return result
