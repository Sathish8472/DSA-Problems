class Solution:

    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = cur_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]
            
            max_sum = max(max_sum, cur_sum)

        return max_sum


    # Brute force
    def maxAscendingSum_1(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = 0

        for i in range(n):
            cur_sum = nums[i]
            for j in range(i + 1, n):
                if nums[j] > nums[j - 1]:
                    cur_sum += nums[j]
                else:
                    break   


            max_sum = max(max_sum, cur_sum)

        return max_sum

        