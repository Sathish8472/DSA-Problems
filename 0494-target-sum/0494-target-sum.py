class Solution:
    def findTargetSumWay2s(self, nums: List[int], target: int) -> int:

        n = len(nums)
        total_sum = sum(nums)
        offset = total_sum

        dp = [[-1] * (2 * target + 1) for _ in range(n)]

        return self._solve(nums, n - 1, target + offset, dp, offset)

    def _solve2(self, nums, ind, current_sum, dp, offset):

        if ind == -1:
            return 1 if current_sum == offset else 0

        if dp[ind][current_sum] != -1:
            return dp[ind][current_sum]

        plus = self._solve(nums, ind - 1, current_sum - nums[ind], dp, offset)
        minus = self._solve(nums, ind - 1, current_sum + nums[ind], dp, offset)

        print(f"plus: {plus}, minus: {minus}")
        dp[ind][current_sum] = plus + minus

        return dp[ind][current_sum]
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totSum = sum(nums)
        self.MOD = int(1e9 + 7)
        n = len(nums)

        if totSum - target < 0:
            return 0

        if (totSum - target) % 2 == 1:
            return 0

        s2 = (totSum - target) // 2

        dp = [[-1 for _ in range(s2 + 1)] for _ in range(n)]

        return self.func(n - 1, s2, nums, dp)

    def func(self, ind, target, arr, dp):
        if ind == 0:
            if target == 0 and arr[0] == 0:
                return 2
            if target == 0 or target == arr[0]:
                return 1
            return 0

        if dp[ind][target] != -1:
            return dp[ind][target]

        notTaken = self.func(ind - 1, target, arr, dp)

        taken = 0
        if arr[ind] <= target:
            taken = self.func(ind - 1, target - arr[ind], arr, dp)

        dp[ind][target] = (notTaken + taken) % self.MOD
        return dp[ind][target]
    