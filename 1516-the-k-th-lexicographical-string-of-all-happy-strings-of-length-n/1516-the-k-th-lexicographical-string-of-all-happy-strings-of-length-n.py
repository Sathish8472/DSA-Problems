class Solution:
    # Backtrack
    # Time: O(2 ^ n * n)
    # Space: O(N)
    def getHappyString(self, n: int, k: int) -> str:
        result = None
        count = 0
        chars = ["a", "b", "c"]

        def backtrack(cur_str):
            nonlocal count, result
            if len(cur_str) == n:
                count += 1
                if count == k:
                    result = "".join(cur_str)
                    return True
                return False

            for ch in chars:
                if cur_str and ch == cur_str[-1]:
                    continue

                if backtrack(cur_str + ch):
                    return True

            return False

        backtrack("")

        return result if result else ""
