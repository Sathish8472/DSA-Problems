class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []

        if not digits:
            return result

        letters = {
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
            if len(cur) == len(digits):
                result.append("".join(cur[:]))
                return

            comb_letter = letters[digits[index]]

            for ch in comb_letter:
                cur.append(ch)
                backtrack(index + 1, cur)
                cur.pop()

        backtrack(0, [])
        return result
