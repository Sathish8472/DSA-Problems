class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        # Check if magazine has enough letters for ransomNote
        for char, count in ransomNote_count.items():
            if magazine_count[char] < count:
                return False

        return True



    # Brute Force 
    def canConstruct_1(self, ransomNote: str, magazine: str) -> bool:
        mFreq_map = {}
        for ch in magazine:
            mFreq_map[ch] = mFreq_map.get(ch, 0) + 1

        for ch in ransomNote:
            if mFreq_map.get(ch, 0) == 0:
                return False
            mFreq_map[ch] -= 1

        return True
