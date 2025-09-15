class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        return self.getAllCombination(0, 0, target, nums)

    
    def getAllCombination(self, ind, currentSum, target, nums):
        if currentSum == target:
            return 1
        
        if currentSum > target:
            return 0

        if ind >= len(nums):
            return 0
        
        take = self.getAllCombination(ind, currentSum + nums[ind], target, nums)
        noTake = self.getAllCombination(ind + 1, currentSum, target, nums)

        return take + noTake