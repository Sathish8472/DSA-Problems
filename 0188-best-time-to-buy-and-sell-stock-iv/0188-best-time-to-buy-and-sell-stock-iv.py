class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        dp = [[[-1 for _ in range(k + 1)] for _ in range(2)] for _ in range(n)]
        ans = self.solve1(0, 0, k, n, prices, dp)

        return ans
    
    def solve1(self, ind, holding, cap, n, prices, dp):
        if ind == n or cap <= 0:
            return 0
        
        if dp[ind][holding][cap] != -1:
            return dp[ind][holding][cap]
        
        profit = 0

        if holding == 0:
            buy = -prices[ind] + self.solve(ind + 1, 1, cap, n, prices, dp)
            skip = 0 + self.solve(ind + 1, 0, cap, n, prices, dp)
            profit = max(buy, skip)
        else:
            sell = prices[ind] + self.solve(ind + 1, 0, cap - 1, n, prices, dp)
            skip = 0 + self.solve(ind + 1, 1, cap, n, prices, dp)
            profit = max(sell, skip)
        
        dp[ind][holding][cap] = profit
        return profit

    def solve(self, ind, holding, cap, n, prices, dp):
        if ind == n or cap <= 0:   # stop if no days left or no transactions left
            return 0
        
        if dp[ind][holding][cap] != -1:
            return dp[ind][holding][cap]
        
        if holding == 0:
            # either buy today or skip
            take = -prices[ind] + self.solve(ind + 1, 1, cap, n, prices, dp)
            skip = self.solve(ind + 1, 0, cap, n, prices, dp)
            profit = max(take, skip)
        else:
            # either sell today (cap-1) or skip
            sell = prices[ind] + self.solve(ind + 1, 0, cap - 1, n, prices, dp)
            skip = self.solve(ind + 1, 1, cap, n, prices, dp)
            profit = max(sell, skip)
        
        dp[ind][holding][cap] = profit
        return profit
