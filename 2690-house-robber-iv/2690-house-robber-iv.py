class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        min_reward, max_reward = 1, max(nums)
        total_houses = len(nums)

        while min_reward < max_reward:
            mid_reward = (min_reward + max_reward) // 2
            possible_thefts = 0

            index = 0
            while index < total_houses:
                if nums[index] <= mid_reward:
                    possible_thefts += 1
                    index += 2
                else:
                    index += 1

            if possible_thefts >= k:
                max_reward = mid_reward
            else:
                min_reward = mid_reward + 1

        return min_reward
    


    def minCapability_1(self, nums: List[int], k: int) -> int:
        max_amount = set()

        def backtrack(index, ds):

            if len(ds) == k:
                max_amount.add(max(ds))
                return

            if index >= len(nums):
                return

            ds.append(nums[index])
            backtrack(index + 2, ds)
            ds.pop()

            backtrack(index + 1, ds)

        backtrack(0, [])

        return min(max_amount) if max_amount else float("inf")
