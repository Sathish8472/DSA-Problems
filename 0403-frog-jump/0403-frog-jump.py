class Solution:
    def __init__(self):
        self.mark = {}
        self.dp = [[-1] * 2001 for _ in range(2001)]

    def solve(self, stones, n, index, prevJump):
        if index == n - 1:
            return True
        if self.dp[index][prevJump] != -1:
            return self.dp[index][prevJump] == 1

        ans = False
        for nextJump in [prevJump - 1, prevJump, prevJump + 1]:
            nextPos = stones[index] + nextJump
            if nextJump > 0 and nextPos in self.mark:
                nextIndex = self.mark[nextPos]
                ans |= self.solve(stones, n, nextIndex, nextJump)

        self.dp[index][prevJump] = 1 if ans else 0
        return ans

    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
        self.mark = {stone: i for i, stone in enumerate(stones)}
        return self.solve(stones, n, 0, 0)
