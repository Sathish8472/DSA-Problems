class Solution:
    def countOdds(self, low: int, high: int) -> int:

        if low % 2 == 0:
            low += 1

        if low > high:
            return 0
        else:
            res = (high - low) // 2
            return res + 1