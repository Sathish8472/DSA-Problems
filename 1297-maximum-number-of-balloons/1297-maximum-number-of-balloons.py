class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_count = Counter(text)
        balloon_count = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}

        return min(
            char_count[ch] // balloon_count[ch] if ch in char_count else 0
            for ch in balloon_count
        )



    # Using Built-in libraries
    def maxNumberOfBalloons_3(self, text: str) -> int:
        count = Counter(text)
        return min(count["b"], count["a"], count["l"] // 2, count["o"] // 2, count["n"])



    # Using Built-in libraries
    def maxNumberOfBalloons_2(self, text: str) -> int:
        balloon_count = Counter("balloon")
        text_count = Counter(text)
        max_instances = float("inf")

        for char in balloon_count:
            max_instances = min(max_instances, text_count[char] // balloon_count[char])

        return max_instances




    # Brute Force
    # Time: O(N ^ 2), Space: O(N)
    def maxNumberOfBalloons_1(self, text: str) -> int:
        target = "balloon"
        count = 0

        while True:
            for ch in target:
                pos = text.find(ch)
                if pos == -1:
                    return count
                text = text[:pos] + text[pos + 1 :]
            count += 1
