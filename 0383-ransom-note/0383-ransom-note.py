class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mFreq_map = {}

        for ch in magazine:
            if ch in mFreq_map:
                mFreq_map[ch] += 1
            else:
                mFreq_map[ch] = 1
        
        print(mFreq_map)
        for ch in ransomNote:
            print(ch)
            if ch in mFreq_map:
                if mFreq_map[ch] > 0:
                    mFreq_map[ch] -= 1
                else:
                    return False
            else:
                return False
        
        print(mFreq_map)
        return True


        