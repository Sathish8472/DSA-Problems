class Solution:

    def minimumDifference(self, nums):
        n = len(nums) // 2
        total = sum(nums)
        left, right = nums[:n], nums[n:]

        left_sums = [set() for _ in range(n+1)]
        right_sums = [set() for _ in range(n+1)]

        for k in range(n+1):
            for comb in combinations(left, k):
                left_sums[k].add(sum(comb))
            for comb in combinations(right, k):
                right_sums[k].add(sum(comb))

        res = float('inf')
        for k in range(n+1):
            l = sorted(left_sums[k])
            r = sorted(right_sums[n-k])
            i, j = 0, len(r)-1
            while i < len(l) and j >= 0:
                s = l[i] + r[j]
                res = min(res, abs((total - s) - s))
                if (total - s) > s:
                    i += 1
                else:
                    j -= 1
        return res




    # Tabulation - Memory issue
    def minimumDifference12(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total = sum(nums)
        max_sum = sum(abs(x) for x in nums)
        offset = max_sum  # To handle negative sums
        # dp[cnt][sum + offset] = True if possible
        dp = [set() for _ in range(n + 1)]
        dp[0].add(0)

        for num in nums:
            # Traverse backwards to avoid using the same number twice
            for cnt in range(n, 0, -1):
                for prev_sum in dp[cnt - 1]:
                    dp[cnt].add(prev_sum + num)

        res = float('inf')
        for s in dp[n]:
            res = min(res, abs((total - s) - s))
        return res

    # Memoization
    def minimumDifference1(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total = sum(nums)
        dp = {}

        return self.func(0, 0, 0, nums, n, total, dp)
    
    def func(self, i, cnt, curr_sum, nums, n, total, dp):
        if cnt > n:
            return float('inf')
        
        if i == len(nums):
            if cnt == n:
                return abs((total - curr_sum) - curr_sum)
            return float('inf')

        key = (i, cnt, curr_sum)
        if key in dp:
            return dp[key]

        pick = self.func(i + 1, cnt + 1, curr_sum + nums[i], nums, n, total, dp)
        not_pick = self.func(i + 1, cnt, curr_sum, nums, n, total, dp)

        dp[key] = min(pick, not_pick)
        return dp[key]