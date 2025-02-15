class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        mFreq_map = {}
        for ch in magazine:
            mFreq_map[ch] = mFreq_map.get(ch, 0) + 1

        for ch in ransomNote:
            if mFreq_map.get(ch, 0) == 0:
                return False
            mFreq_map[ch] -= 1

        return True
