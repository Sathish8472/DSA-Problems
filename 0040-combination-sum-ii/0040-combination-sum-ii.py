class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
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
