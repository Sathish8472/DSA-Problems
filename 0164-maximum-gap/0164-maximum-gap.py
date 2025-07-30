class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        max_val = float('-inf')
        n = len(nums)

        if n < 2:
            return 0

        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            max_val = max(max_val, diff)
        
        return max_val
