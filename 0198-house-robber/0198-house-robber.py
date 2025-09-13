class Solution:

    # Space Optmization
    # Time: O(N), Space: Constant
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        if n == 1:
            return nums[0]
        
        prev2 = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, n):
            rob = nums[i] + prev2
            no_rob = prev

            curi = max(rob, no_rob)
            prev2 = prev
            prev = curi
        
        return prev
    

    # DP - Memorization - Buttom up
    # Time: O(N), 
    # Space: O(N)
    def rob2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [-1] * (n + 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])       # Important

        for i in range(2, n):
            rob = nums[i] + dp[i - 2]
            no_rob = dp[i - 1]

            dp[i] = max(rob, no_rob)

        return dp[n - 1]
        

    # DP - Memoization - Top down 
    # Time: O(N), SPace : O(N)
    def rob_2(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n + 1)

        def _rob(self, nums: List[int], ind: int, dp) -> int:
            if ind < 0:
                return 0
            
            if dp[ind] != -1:
                return dp[ind]

            rob = nums[ind] + self._rob(nums, ind - 2, dp)
            no_rob = self._rob(nums, ind - 1, dp)
            dp[ind] = max(rob, no_rob)

            return dp[ind]

        return _rob(nums, n - 1, dp)


    # Recursion => Time: 2 ^ n, Space: O(N)
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        return self._helper(nums, n - 1)

    def _helper(self, nums: List[int], i):
        if i < 0:
            return 0

        rob = nums[i] + self._helper(nums, i - 2)
        no_rob = self._helper(nums, i - 1)

        return max(rob, no_rob)
