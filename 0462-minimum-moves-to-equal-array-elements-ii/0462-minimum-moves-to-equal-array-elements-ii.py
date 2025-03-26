class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        nums.sort()

        n = len(nums)
        median = nums[n // 2]

        count = 0

        for num in nums:
            count += abs(median - num)
        
        return count