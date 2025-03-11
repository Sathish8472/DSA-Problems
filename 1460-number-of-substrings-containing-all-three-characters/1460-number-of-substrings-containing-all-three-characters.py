class Solution:

    # Sliding window
    # Time: O(N), Space: O(1)
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        freq = {'a': 0, 'b': 0, 'c': 0}
        left = 0

        for right in range(len(s)):
            freq[s[right]] += 1

            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                count += len(s) - right
                freq[s[left]] -= 1
                left += 1

        return count

    # Brute Force
    # Time: O(N ^ 2)
    def numberOfSubstrings1(self, s: str) -> int:
        count = 0
        unique_chars = {"a", "b", "c"}

        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                seen.add(s[j])
                if seen == unique_chars:
                    count += 1

        return count
