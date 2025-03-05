class Solution:

    # Optimal
    # Time: O(1), Space: O(1)
    def coloredCells(self, n: int) -> int:
        return 2 * n * (n - 1) + 1

    # Not Efficient
    # time: O(N)
    def coloredCells1(self, n: int) -> int:

        def getCombination(n1):
            if n1 == 1:
                return 1

            return (n1 - 1) * 4 + getCombination(n1 - 1)

        return getCombination(n)
