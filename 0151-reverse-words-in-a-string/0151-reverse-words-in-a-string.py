class Solution:
    # In-place Efficient Approach
    def reverseWords(self, s: str) -> str:
        s = list(s)
        self.reverse(s, 0, len(s) - 1)
        self.reverse_each_word(s)

        return ''.join(self.clean_spaces(s))

    def reverse(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverse_each_word(self, s):
        n = len(s)
        start = 0
        while start < n:
            while start < n and s[start] == ' ':
                start += 1
            
            end = start
            while end < n and s[end] != ' ':
                end += 1
            
            self.reverse(s, start, end - 1)

            start = end

    def clean_spaces(self, s):
        n = len(s)
        result = []
        in_word = False
        for i in range(n):
            if s[i] != ' ':
                if not in_word:
                    result.append(' ') if result else None  # Add a single space before a new word
                    in_word = True
                result.append(s[i])
            else:
                in_word = False
        return result








    # Brute
    # Time: O(N), Space: O(N)
    def reverseWords_2(self, s: str) -> str:
        words = [word for word in s.split(" ") if word]
        return " ".join(reversed(words))


    def reverseWords_1(self, s: str) -> str:
        return " ".join(reversed(s.split()))