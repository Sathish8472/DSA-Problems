class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()
        print(nums)
        visited = [False] * n

        def backtrack(current_subset):
            nonlocal result

            if len(current_subset) == n:
                result.append(current_subset[:])
                return 

            for i in range(n):
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                if not visited[i]:
                    current_subset.append(nums[i])
                    visited[i] = True
                    backtrack(current_subset)
                    current_subset.pop()
                    visited[i] = False


        backtrack([])
        return result

    # Backtracking Approach
    # Time: O(n! + n log n), Space: O(N!)
    def permuteUnique1(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # O(N Log N)
        visited = [False] * len(nums)

        # Time O(N!), Space: O(N!)
        def backtrack(curr_perm):
            if len(curr_perm) == len(nums):
                result.append(curr_perm[:])
                return

            for i, num in enumerate(nums):
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                if not visited[i]:
                    curr_perm.append(num)
                    visited[i] = True
                    backtrack(curr_perm)
                    curr_perm.pop()
                    visited[i] = False

        backtrack([])
        return result
