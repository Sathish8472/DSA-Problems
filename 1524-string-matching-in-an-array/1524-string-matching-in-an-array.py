class Solution:

    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)  # Sort words by length
        result = []

        for i in range(len(words)):
            for j in range(i + 1, len(words)):  # Only check longer words
                if words[i] in words[j]:
                    result.append(words[i])
                    break  # No need to check further

        return result

    # Brute force
    # Time: O(n² * m) , Space: O(N)
    def stringMatching1(self, words: List[str]) -> List[str]:
        result = []

        for word in words:
            for other in words:
                if (
                    word != other and word in other
                ):  # Check if word is a substring of another
                    result.append(word)
                    break

        return result
