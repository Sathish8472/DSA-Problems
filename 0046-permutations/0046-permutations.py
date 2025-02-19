class Solution:

    # Optmized code
    # Time: O(N!), Space: O(N)
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(cur_perm):
            if len(cur_perm) == len(nums):
                result.append(cur_perm[:])
                return

            for num in nums:
                if num in cur_perm:
                    continue
                cur_perm.append(num)
                backtrack(cur_perm)
                cur_perm.pop()

        backtrack([])
        return result




    def permute1(self, nums: List[int]) -> List[List[int]]:
        result = []
        ds = []
        freq = [False] * len(nums)

        def generatePermute():
            if len(ds) == len(nums):
                result.append(
                    ds[:]
                )  # Adds a copy of the current permutation to result (to avoid reference issues).
                return

            for i, num in enumerate(nums):
                if not freq[i]:
                    freq[i] = True
                    ds.append(num)
                    generatePermute()
                    freq[i] = False
                    ds.pop()

        generatePermute()
        return result
