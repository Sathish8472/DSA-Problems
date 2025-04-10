class Solution:


    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n + 1)
        dp[0] 
        return self._rob(nums, n - 1, dp)

        
    def _rob(self, nums: List[int], i, dp):
        if i < 0:
            return 0

        if dp[i] != -1:
            return dp[i]

        rob = nums[i] + self._rob(nums, i - 2, dp)
        no_rob = self._rob(nums, i - 1, dp)

        dp[i] = max(rob, no_rob)
        return dp[i]



        

    def rob_1(self, nums: List[int]) -> int:

        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        n = len(nums)
        even_house_amt = 0
        
        for i in range(0, n, 2):
            print(i)
            even_house_amt += nums[i]

        odd_house_amt = 0
        
        for i in range(1, n, 2):
            print(i)
            odd_house_amt += nums[i]

        return max(even_house_amt, odd_house_amt)


        