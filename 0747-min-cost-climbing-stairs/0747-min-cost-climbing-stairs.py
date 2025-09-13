class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
    
        def _helper(ind):
            if ind >= len(cost):
                return 0
            
            jumpOne = cost[ind] + _helper(ind + 1)
            jumpTwo = cost[ind] + _helper(ind + 2)

            return min(jumpOne, jumpTwo)

        return min(_helper(0), _helper(1))
        