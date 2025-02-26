class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = float('-inf')

        for i in range(len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)

        return max_sum

    # backtrack, Not Efficient
    # Time: O(N ^ 2), Space: O(N)
    def maxSubArray_1(self, nums: List[int]) -> int:
        maxSum = float('-inf')

        def backtrack(start, end):
            nonlocal maxSum

            if end > len(nums):
                return
            
            current_subarray = nums[start:end]
            current_sum = sum(current_subarray)
            maxSum = max(maxSum, current_sum)
            
            backtrack(start, end + 1)

        for i in range(len(nums)):
            backtrack(i, i + 1)

        return maxSum
        