class Solution:

    # DP code - Kadane's algm - Optimal
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_sum = float('-inf')

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum
    


    # Divide & Conquer
    # time: O(n log n), Space: O(n log n)
    def maxSubArray_22(self, nums: list[int]) -> int:

        def helper(left, right):
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            leftMax = helper(left, mid)
            rightMax = helper(mid + 1, right)
            
            # Find max crossing sum
            leftSum = float('-inf')
            tempSum = 0
            for i in range(mid, left - 1, -1):
                tempSum += nums[i]
                leftSum = max(leftSum, tempSum)

            rightSum = float('-inf')
            tempSum = 0
            for i in range(mid + 1, right + 1):
                tempSum += nums[i]
                rightSum = max(rightSum, tempSum)

            crossMax = leftSum + rightSum
            return max(leftMax, rightMax, crossMax)
        
        return helper(0, len(nums) - 1)


    # DP array
    # time: O(N), Space: O(N)
    def maxSubArray_2(self, nums: list[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        maxSum = dp[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            maxSum = max(maxSum, dp[i])

        return maxSum


    # backtrack, Not Efficient
    # Time: O(N ^ 2), Space: O(N)
    def maxSubArray_1(self, nums: List[int]) -> int:
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