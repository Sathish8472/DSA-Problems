class Solution:
    def coloredCells(self, n: int) -> int:

        def getCombination(n1):
            if n1 == 1:
                return 1

            return (n1 - 1) * 4 + getCombination(n1 - 1)

        return getCombination(n)
        