class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken_set = set(brokenLetters)
        count = 0

        words = text.split(" ")
        for word in words:
            if all(ch not in broken_set for ch in word):
                count += 1
                
        return count