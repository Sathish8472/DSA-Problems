from collections import defaultdict

class Solution:
    def countOfSubstrings1(self, word: str, k: int) -> int:
        n = len(word)
        vowels = set("aeiou")
        vowel_count = defaultdict(int)
        cons_count = 0
        valid_substr_count = 0
        left = 0

        for right in range(n):
            char = word[right]
            if char in vowels:
                vowel_count[char] += 1
            else:
                cons_count += 1

            # Adjust left pointer while we have more than k consonants
            while cons_count > k:
                left_char = word[left]
                if left_char in vowels:
                    vowel_count[left_char] -= 1
                    if vowel_count[left_char] == 0:
                        del vowel_count[left_char]
                else:
                    cons_count -= 1
                left += 1

            # Count valid substrings with exactly k consonants and all vowels
            temp_left = left
            while cons_count == k and len(vowel_count) == 5:
                valid_substr_count += 1
                left_char = word[temp_left]
                if left_char in vowels:
                    vowel_count[left_char] -= 1
                    if vowel_count[left_char] == 0:
                        del vowel_count[left_char]
                else:
                    cons_count -= 1
                temp_left += 1

            # Restore left pointer for the next iteration
            left = temp_left

        return valid_substr_count

    def _isVowel(self, c: str) -> bool:
        return c in "aeiou"

    def countOfSubstrings(self, word: str, k: int) -> int:
        num_valid_substrings = 0
        start = end = 0
        vowel_count = {}  # Dictionary to keep counts of vowels
        consonant_count = 0  # Count of consonants
        next_consonant = [0] * len(word)  # Array for next consonant indices
        next_consonant_index = len(word)

        # Fill next_consonant array
        for i in range(len(word) - 1, -1, -1):
            next_consonant[i] = next_consonant_index
            if not self._isVowel(word[i]):
                next_consonant_index = i

        while end < len(word):
            new_letter = word[end]
            if self._isVowel(new_letter):
                vowel_count[new_letter] = vowel_count.get(new_letter, 0) + 1
            else:
                consonant_count += 1

            # Shrink window if too many consonants are present
            while consonant_count > k:
                start_letter = word[start]
                if self._isVowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1
                start += 1

            # Count valid substrings with all vowels and exactly k consonants
            while start < len(word) and len(vowel_count) == 5 and consonant_count == k:
                num_valid_substrings += next_consonant[end] - end
                start_letter = word[start]
                if self._isVowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1
                start += 1

            end += 1

        return num_valid_substrings

