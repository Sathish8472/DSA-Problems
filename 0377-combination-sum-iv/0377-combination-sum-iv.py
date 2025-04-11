class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
                
        return dp[-1]


    def combinationSum4_1(self, nums: List[int], target: int) -> int:

        self.counts = 0

        def comb(tar):
            if tar == 0:
                self.counts += 1
            for num in nums:
                if num > tar:
                    break
                comb(tar - num)
        
        comb(target)

        return self.counts
        