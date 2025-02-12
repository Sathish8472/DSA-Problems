# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        # Helper function to count the number of matching characters between two words
        def count_matching_chars(word1: str, word2: str) -> int:
            return sum(c1 == c2 for c1, c2 in zip(word1, word2))

        # Helper function to find the word with the most overlap with other words
        def find_best_guess(candidates: List[str]) -> str:
            # Create a frequency count of characters at each position in the words
            char_frequency = [[0 for _ in range(26)] for _ in range(6)]  # 6 positions, 26 letters
            for word in candidates:
                for i, char in enumerate(word):
                    char_frequency[i][ord(char) - ord('a')] += 1

            # Evaluate the word with the highest overlap score
            best_overlap_score = -1
            best_guess = ""
            for word in candidates:
                overlap_score = sum(char_frequency[i][ord(char) - ord('a')] for i, char in enumerate(word))
                if overlap_score > best_overlap_score:
                    best_overlap_score = overlap_score
                    best_guess = word

            return best_guess

        # Start with the full list of words as candidates
        candidates = words[:]

        # Loop until we either guess the secret word or run out of candidates
        while candidates:
            # Guess the word with the most overlap with others
            guess = find_best_guess(candidates)

            # Make a guess using the Master API
            matches = master.guess(guess)

            # If we guessed the secret word, we're done
            if matches == 6:
                return

            # Filter candidates to keep only those with the same number of matching characters as the guess
            candidates = [word for word in candidates if count_matching_chars(guess, word) == matches]