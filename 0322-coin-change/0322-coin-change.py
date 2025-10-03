class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]

        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = float('inf')
            
        for ind in range(1, n):
            for target in range(amount + 1):
                
                not_take = 0 + dp[ind - 1][target]
                
                take = float('inf')
                if coins[ind] <= target:
                    take = 1 + dp[ind][target - coins[ind]]
                
                dp[ind][target] = min(not_take, take)
        
        result = dp[n - 1][amount]
        if result >= float('inf'):
            return -1

        return result

    
    # Dp - Memoization - Top  down approach
    # Time: O(N * K)
    # Space: O(N * K) + O(K)
    def coinChange_1(self, coins: List[int], amount: int) -> int:
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
