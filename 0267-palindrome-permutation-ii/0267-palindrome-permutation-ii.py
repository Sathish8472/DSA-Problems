class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        result = []
        s = sorted(s)
        n = len(s)
        visited = [False] * n

        def isPalindrom(str):
            
            n = len(str)
            for i in range(n // 2):
                if str[i] != str[n - i - 1]:
                    return False
            
            return True

        def backtrack(current_str):

            if len(current_str) == len(s):
                str2 = "".join(current_str)
                if isPalindrom(str2):
                    result.append(str2)
                return 

            for i, ch in enumerate(s):
                if i > 0 and s[i] == s[i - 1] and not visited[i - 1]:
                    continue
                
                if not visited[i]:
                    current_str.append(ch)
                    visited[i] = True
                    backtrack(current_str)
                    current_str.pop()
                    visited[i] = False

        backtrack([])
        return result