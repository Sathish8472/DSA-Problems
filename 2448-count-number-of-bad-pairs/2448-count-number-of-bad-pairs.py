class Solution:

    # HashMap Approach
    def countBadPairs(self, nums: List[int]) -> int: 
        good_pairs = 0
        n = len(nums)
        diff_count = defaultdict(int)

        for i in range(n):
            diff = nums[i] - i
            if diff in diff_count:
                good_pairs += diff_count[diff]
            diff_count[diff] += 1

        total_pairs = n * (n - 1) // 2
        bad_pairs = total_pairs - good_pairs

        return bad_pairs


    # Brute Force
    def countBadPairs_1(self, nums: List[int]) -> int:
        bad_pair_count = 0
        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                if j - i != nums[j] - nums[i]:
                    bad_pair_count += 1

        return bad_pair_count
        