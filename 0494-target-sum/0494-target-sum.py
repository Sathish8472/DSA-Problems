class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)
        s1 = (target + totalSum) // 2
        n = len(nums)

        return self.solve(n - 1, s1, nums)

    
    def solve(self, ind, target, nums):
        if ind == 0:
            if target == 0 and nums[ind] == 0:
                return 2

            if target == 0 or nums[ind] == 0 or target == nums[ind]:
                return 1
            return 0

        take = 0
        if nums[ind] <= target:
            take = self.solve(ind - 1, target - nums[ind], nums)

        skip = self.solve(ind - 1, target, nums)

        return take + skip
