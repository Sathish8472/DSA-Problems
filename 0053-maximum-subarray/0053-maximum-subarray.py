class Solution:

    # Optimal
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = float('-inf')

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
    


    # backtrack, Not Efficient
    # Time: O(N ^ 2), Space: O(N)
    def maxSubArray1(self, nums: List[int]) -> int:
        max_sum = float('-inf')

        def backtrack(start, end):
            nonlocal max_sum

            if end > len(nums):
                return 
            
            current_subarray = nums[start:end]
            current_sum = sum(current_subarray)
            max_sum = max(max_sum, current_sum)

            backtrack(start, end + 1)

        for i in range(len(nums)):
            backtrack(i, i + 1)

        return max_sum  