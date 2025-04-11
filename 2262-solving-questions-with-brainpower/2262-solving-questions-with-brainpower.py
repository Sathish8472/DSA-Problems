class Solution:


    # DP - Memoization 
    # Time: O(N)
    # Space: O(N)
    def mostPoints(self, questions: List[List[int]]) -> int:

        dp = [-1] * (len(questions) + 1)
        return self._solve(questions, 0, dp)
        
    def _solve(self, questions, ind, dp) -> int:
        if ind >= len(questions):
            return 0

        if dp[ind] != -1:
            return dp[ind]

        quest = questions[ind]
        solve = quest[0] + self._solve(questions, ind + quest[1] + 1, dp)
        skip = 0 + self._solve(questions, ind + 1, dp)

        dp[ind] = max(solve, skip)
        
        return dp[ind]


    
    # Recursion
    # Time: 2 ^ n, exponential time
    # Space: O(N) recursion stack space
    def mostPoints_1(self, questions: List[List[int]]) -> int:
        return self._solve(questions, 0)
        
    def _solve2(self, questions, ind) -> int:
        if ind >= len(questions):
            return 0

        quest = questions[ind]
        solve = quest[0] + self._solve(questions, ind + quest[1] + 1)
        skip = 0 + self._solve(questions, ind + 1)

        return max(solve, skip)
        