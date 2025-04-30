class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.func(0, candidates, [], target, result)
        return result

    def func(self, ind, nums, current_sub, current_sum, result):

        if current_sum < 0:
            return 
        
        if current_sum == 0:
            result.append(current_sub[:])
            return 
        
        if ind == len(nums):
            return
        
        current_sub.append(nums[ind])
        current_sum -= nums[ind]
        
        self.func(ind, nums, current_sub, current_sum, result)
        current_sum += nums[ind]
        current_sub.pop()
        self.func(ind + 1, nums, current_sub, current_sum, result)

        return


    # Backtrack
    # Time: O(2 ^ n)
    # Space Complexity: O(T) (due to recursion depth) + O(k) (to store results, where k is the number of combinations)
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(index, current, target):
            if target == 0:
                result.append(current[:])
                return

            for i in range(index, len(candidates)):
                if candidates[i] > target:
                    continue
                current.append(candidates[i])
                backtrack(i, current, target - candidates[i])
                current.pop()

        backtrack(0, [], target)
        return result
