class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        self.func(0, target, [], candidates, ans)
        return ans

    
    def func2(self, ind, nums, current_sub, current_sum, result):

        if current_sum < 0:
            return
        
        if current_sum == 0:
            result.append(current_sub[:])
            return
        
        if ind == len(nums):
            return

        current_sub.append(nums[ind])
        current_sum -= nums[ind]
        take = self.func(ind + 1, nums, current_sub, current_sum, result)
        current_sub.pop()
        current_sum += nums[ind]

        no_take = self.func(ind + 1, nums, current_sub, current_sum, result)

        for i in range(ind, len(nums)):
            num = nums[i]

            if i > ind :
                return

        return 

    def func(self, ind, sum, nums, candidates, ans):
        # If the sum is zero, add the current combination to the result
        if sum == 0:
            ans.append(nums[:])
            return
        
        # If the sum is negative or we have exhausted the candidates, return
        if sum < 0 or ind == len(candidates):
            return
        
        # Include the current candidate
        nums.append(candidates[ind])
        
        # Recursively call with updated sum and next index
        self.func(ind + 1, sum - candidates[ind], nums, candidates, ans)
        
        # Backtrack by removing the last added candidate
        nums.pop()
        
        # Skip duplicates: if not picking the current candidate, 
        # ensure the next candidate is different
        for i in range(ind + 1, len(candidates)):
            if candidates[i] != candidates[ind]:
                self.func(i, sum, nums, candidates, ans)
                break





    def combinationSum22(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(index, current, target):
            if target == 0:
                result.append(current[:])
                return

            for i in range(index, len(candidates)):
                candidate = candidates[i]

                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                if candidate > target:
                    break

                current.append(candidate)
                backtrack(i + 1, current, target - candidate)
                current.pop()

        backtrack(0, [], target)
        return result
