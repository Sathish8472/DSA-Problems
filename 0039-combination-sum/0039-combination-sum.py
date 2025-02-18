class Solution:

    # Backtrack
    # Time: O(2 ^ n)
    # Space Complexity: O(T) (due to recursion depth) + O(k) (to store results, where k is the number of combinations)
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
