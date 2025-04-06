class Solution:

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        if n == 0:
            return []

        dp = [1] * n
        hash_arr = list(range(n))

        for i in range(n):
            for prev_index in range(i):
                if nums[i] % nums[prev_index] == 0 and 1 + dp[prev_index] > dp[i]:
                    dp[i] = 1 + dp[prev_index]
                    hash_arr[i] = prev_index
        
        ans = -1
        last_index = -1

        for i in range(n):
            if dp[i] > ans:
                ans = dp[i]
                last_index = i

        result = [nums[last_index]]

        while hash_arr[last_index] != last_index:
            last_index = hash_arr[last_index]
            result.append(nums[last_index])
        
        return result



    # Brute 
    def largestDivisibleSubset_1(self, nums: List[int]) -> List[int]:

        nums.sort()
        self.largest_subset = []
        self._generate_all_possible_subset(nums, 0, [])

        return self.largest_subset

    def _generate_all_possible_subset(self, nums: List[int], start_index, current_subset) -> None:
        
        if self._is_divisible_subset(current_subset):
            if len(self.largest_subset) < len(current_subset):
                self.largest_subset = current_subset[:]

        for i in range(start_index, len(nums)):
            current_subset.append(nums[i])
            self._generate_all_possible_subset(nums, i + 1, current_subset)
            current_subset.pop()
        
    def _is_divisible_subset(self, subset: List[int]) -> bool:

        if not subset:
            return False
        
        for i in range(1, len(subset)):
            if subset[i] % subset[i - 1] != 0:
                return False

        return True