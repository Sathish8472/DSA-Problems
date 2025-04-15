class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        dp = [[-1] * (amount + 1) for _ in range(n)]

        result = self._solve(coins, n - 1, amount, dp)

        if result >= int(1e9):
            return -1

        return result
    
    def _solve(self, coins, ind, k, dp):

        if ind == 0:
            if k % coins[0] == 0:
                return k // coins[0]
            else:
                return float('inf')
        
        if dp[ind][k] != -1:
            return dp[ind][k]
            
        take = float('inf')
        if coins[ind] <= k:
            take = 1 + self._solve(coins, ind, k - coins[ind], dp)

        not_taken = 0 + self._solve(coins, ind - 1, k, dp)

        dp[ind][k] = min(take, not_taken) 

        return dp[ind][k]
