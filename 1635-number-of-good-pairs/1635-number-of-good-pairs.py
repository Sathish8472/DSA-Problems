class Solution:

    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        freq_map = defaultdict(int)

        for num in nums:
            count += freq_map[num]
            freq_map[num] += 1

        return count




    # Brute-force
    def numIdenticalPairs_1(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    count += 1

        return count
