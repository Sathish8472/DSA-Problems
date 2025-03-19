class Solution:
    
    def countPalindromicSubsequence(self, s: str) -> int:
        unique_count = 0

        for ch in set(s):
            left, right = s.find(ch), s.rfind(ch)
            if left < right:
                unique_count += len(set(s[left + 1: right]))
        
        return unique_count






    def countPalindromicSubsequence_1(self, s: str) -> int:
        result = set()

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                for k in range(j + 1, len(s)):
                    substr = s[i] + s[j] + s[k]
                    if s[i] == s[k]:
                        result.add(substr)
                        
        print(result)
        return len(result)



        