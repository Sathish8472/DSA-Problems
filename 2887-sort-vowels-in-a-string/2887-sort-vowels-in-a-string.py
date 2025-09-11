class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")

        sorted_vowels = sorted([ch for ch in s if ch in vowels])
        
        
        result = []
        vowel_index = 0

        for ch in s:
            if ch in vowels:
                result.append(sorted_vowels[vowel_index])
                vowel_index += 1
            else:
                result.append(ch)
        
        return "".join(result)