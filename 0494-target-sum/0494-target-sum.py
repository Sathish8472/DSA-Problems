class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)

        if abs(target) <= totalSum:
            return 0
        
        if (totalSum + target) % 2 != 0:
            return 0

        s1 = (target + totalSum) // 2
        n = len(nums)

        dp = [[-1] *(s1 + 1) for _ in range(n)]

        return self.solve(n - 1, s1, nums, dp)

    def solve(self, ind, target, nums, dp):
        if ind == 0:
            if target == 0 and nums[ind] == 0:
                return 2

            if target == 0 or target == nums[ind]:
                return 1
            return 0

        if dp[ind][target] != -1:
            return dp[ind][target]
            
        take = 0
        if nums[ind] <= target:
            take = self.solve(ind - 1, target - nums[ind], nums, dp)

        skip = self.solve(ind - 1, target, nums, dp)

        dp[ind][target] = take + skip
        return dp[ind][target]
