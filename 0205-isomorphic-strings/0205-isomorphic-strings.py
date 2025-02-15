class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            # Check if current character in s has been mapped to a different character in t
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False
            # Check if current character in t has been mapped to a different character in s
            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False

            # Create the mapping from s to t and from t to s
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True