class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        dp = [-1] * (n + 1)

        def _helper(ind):
            if ind >= len(cost):
                return 0
            
            if dp[ind] != -1:
                return dp[ind]

            jumpOne = cost[ind] + _helper(ind + 1)
            jumpTwo = cost[ind] + _helper(ind + 2)

            dp[ind] = min(jumpOne, jumpTwo)
            return dp[ind]

        return min(_helper(0), _helper(1))


    def minCostClimbingStairs1(self, cost: List[int]) -> int:
        n = len(cost)
    
        def _helper(ind):
            if ind >= len(cost):
                return 0
            
            jumpOne = cost[ind] + _helper(ind + 1)
            jumpTwo = cost[ind] + _helper(ind + 2)

            return min(jumpOne, jumpTwo)

        return min(_helper(0), _helper(1))
        