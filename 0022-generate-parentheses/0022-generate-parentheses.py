class Solution:
    # Backtracking (Recursive Approach)
    # Time: O(4ⁿ / √n), Space: O(N)
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(current, openCount, closeCount):
            if len(current) == 2 * n:
                result.append(current)
                return

            if openCount < n:
                backtrack(current + "(", openCount + 1, closeCount)

            if closeCount < openCount:
                backtrack(current + ")", openCount, closeCount + 1)

        backtrack("", 0, 0)
        return result
