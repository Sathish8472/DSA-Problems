class Solution:

    # In-place
    def reverseWords_2(self, s: str) -> str:
        s = s.strip()
        s = list(s)
        self.reverse(s, 0, len(s) - 1)
        print(s)

    # Brute
    def reverseWords_1(self, s: str) -> str:
        words = [word for word in s.split(" ") if word]
        return " ".join(reversed(words))


    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))