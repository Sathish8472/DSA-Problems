class Solution:

    # Backtrack
    # Time: O(4 ^ n * n), SpacE: O(4 ^ n)
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        if not digits:                              # O(1)
            return result                           # O(1)

        letters = {                                 # O(1)
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, cur):
            if len(cur) == len(digits):             # O(1)
                result.append("".join(cur[:]))      # O(k) - Convert list to string (k = len of cur)
                return
            
            for ch in letters[digits[index]]:       # O(1) - Access dict, O(4) max 4 letters per digit)
                cur.append(ch)                      # O(1) - Add character to list
                backtrack(index + 1, cur)           # Recursive call
                cur.pop()                           # O(1) - Backtracking step

        backtrack(0, [])                            # Start recursion
        return result                               # O(1)
