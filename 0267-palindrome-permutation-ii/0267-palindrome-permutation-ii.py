class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        possible, half_str, middle_char = self.can_be_palindrome(s)

        if not possible:
            return []
        
        return self._generate_palindrome(half_str, middle_char)
    
    def _generate_palindrome(self, half: str, middle: str) -> List[str]:
        result = []
        n = len(half)
        visited = [False] * n

        def backtrack(curr_perm):
            if len(curr_perm) == n:
                palindrome = curr_perm + middle + curr_perm[::-1]
                result.append(palindrome)
                return
            
            for i in range(n):
                if visited[i]:
                    continue
                
                if i > 0 and half[i] == half[i - 1] and not visited[i - 1]:
                    continue
                
                visited[i] = True
                backtrack(curr_perm + half[i])
                visited[i] = False

        backtrack("")
        return result

    def can_be_palindrome(self, s: str) -> tuple[bool, str, str]:
        char_counts = {}

        for char in s:
            char_counts[char] = char_counts.get(char, 0) + 1
        
        odd_chars = []
        for char, count in char_counts.items():
            if count % 2 != 0:
                odd_chars.append(char)
            
        if len(odd_chars) > 1:
            return False, "", ""
        
        middle_char = odd_chars[0] if odd_chars else ""

        half_chars = []

        for char, count in char_counts.items():
            half_chars.extend([char] * (count // 2))
        
        print(half_chars)

        return True, "".join(sorted(half_chars)), middle_char


    def generatePalindromes_1(self, s: str) -> List[str]:
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