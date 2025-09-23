class Solution:

    # Space optmizatio
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False
        
        k = total_sum // 2
        prev = [False] * (k + 1)
        prev[0] = True

        if nums[0] <= k:
            prev[nums[0]] = True
        
        for ind in range(1, n):
            cur = [False] * (k + 1)
            cur[0] = True

            for target in range(1, k + 1):
                notTaken = prev[target]
                
                taken = False

                if nums[ind] <= target:
                    taken = prev[target - nums[ind]]

                cur[target] = notTaken or taken
            
            prev = cur
        
        return prev[k]


    # Tabulation
    def canPartition2(self, nums: List[int]) -> bool:
        n = len(nums)
        arr = nums
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False
        
        k = total_sum // 2

        dp = [[False] * (k + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True
        
        if arr[0] <= k:
            dp[0][arr[0]] = True
        
        for i in range(1, n):
            for target_val in range(1, k + 1):
                not_taken = dp[i - 1][target_val]

                taken = False
                if arr[i] <= target_val:
                    taken = dp[i - 1][target_val - arr[i]]
                
                dp[i][target_val] = not_taken or taken
        
        return dp[n - 1][k]

    
    # DP - MEmoization
    # Time: O(N * K)
    # Space: O(N + K)
    def canPartition_2(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False

        n = len(nums)
        dp = [[-1] * ((total_sum // 2) + 1) for _ in range(n)]
        return self._solve(nums, n - 1, total_sum // 2, dp)

    
    def _solve(self, nums, ind, target, dp):
        if target == 0:
            return True
        
        if ind == 0:
            return nums[0] == target

        if dp[ind][target] != -1:
            return dp[ind][target]

        pick = False
        if nums[ind] <= target:
            pick = self._solve(nums, ind - 1, target - nums[ind], dp)

        not_pick = self._solve(nums, ind - 1, target, dp)

        dp[ind][target] = pick or not_pick

        return dp[ind][target]



    # Brute - BAcktracking/REcursion
    def canPartition1(self, nums: List[int]) -> bool:
        self.result = False
        nums.sort()
        total_sum = sum(nums)
        print(total_sum)
        self._generate_all_possible_combinations(nums, 0, [], total_sum)

        return self.result

    def _generate_all_possible_combinations(self, nums: List[int], start_index, current_subset, total_sum: int) -> bool:

        if len(current_subset) > 0:
            current_sum = sum(current_subset)
            if current_sum * 2 == total_sum:
                print(current_subset)
                self.result = True
                return

        for i in range(start_index, len(nums)):
            current_subset.append(nums[i])
            self._generate_all_possible_combinations(nums, i + 1, current_subset, total_sum)
            current_subset.pop()
        
        