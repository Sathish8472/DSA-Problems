class Solution:
    def firstMissingPositive_1(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False] * (n + 1)

        print(seen)

        for num in nums:
            if 0 < num <= n:
                seen[num] = True

        for i in range(1, n + 1):
            if not seen[i]:
                return i

        return n + 1
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set(nums)
        expected = 1

        while expected in num_set:
            expected += 1
        return expected

        
    # Brute force
    # Gets failed for many cases
    def firstMissingPositive_1(self, nums: List[int]) -> int:
        n = len(nums)
        nums = list(set(nums))
        expected = 1

        for num in nums:
            if num == expected:
                expected += 1

        return expected
