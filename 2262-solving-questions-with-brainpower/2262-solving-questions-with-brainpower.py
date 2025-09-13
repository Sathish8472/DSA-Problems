class Solution:
    
    # Tabulation, Time: O(N), Space: O(N)
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        
        for i in range(n - 1, -1, -1):
            point, bp = questions[i]
            solve = point + (dp[i + bp + 1] if i + bp + 1 < n else 0)
            skip = dp[i + 1]

            dp[i] = max(solve, skip)

        return dp[0]

    # Memoization, Time: O(N), Space: O(N) + O(N) stack and dp array
    def mostPoints2(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [-1] * (n + 1)

        def _helper(ind):
            if ind >= n:
                return 0
            
            if dp[ind] != -1:
                return dp[ind]

            point, brainPower = questions[ind] 

            solve = point + _helper(ind + brainPower + 1)
            skip = _helper(ind + 1)

            dp[ind] = max(solve, skip)
            return dp[ind]

        return _helper(0)


    # Recursion, Time: 2 ^ n, Space: O(N) stack
    def mostPoints1(self, questions: List[List[int]]) -> int:
        n = len(questions)

        def _helper(ind):
            if ind >= n:
                return 0

            point, brainPower = questions[ind] 

            solve = point + _helper(ind + brainPower + 1)
            skip = _helper(ind + 1)

            return max(solve, skip)

        return _helper(0)


        