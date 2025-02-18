class Solution:
    # Backtrack
    # Time: O(9 ^ K), Space: O(K)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, current, target):
            if len(current) == k and target == 0:
                result.append(current[:])
                return

            if len(current) > k or target < 0:
                return

            for i in range(start, 10):
                current.append(i)
                backtrack(i + 1, current, target - i)
                current.pop()

        backtrack(1, [], n)
        return result
