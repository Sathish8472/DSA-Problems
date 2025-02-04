class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        cur_sum = nums[0]

        for start in range(1, len(nums)):
            if nums[start] <= nums[start - 1]:
                max_sum = max(max_sum, cur_sum)
                cur_sum = 0
            
            cur_sum += nums[start]

        
        return max(max_sum, cur_sum)

        