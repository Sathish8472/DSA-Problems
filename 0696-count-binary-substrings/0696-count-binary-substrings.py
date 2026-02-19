class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        c = prev_c = res = 0
        prev_ch = '~'
        
        for ch in s:
            if prev_ch == ch:
                c += 1
            else:
                res += min(prev_c, c)
                prev_c = c
                c = 1
                prev_ch = ch
        
        res += min(prev_c, c)
        return res