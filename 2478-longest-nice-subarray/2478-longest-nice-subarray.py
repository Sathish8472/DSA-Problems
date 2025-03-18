class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        bitmask = 0
        max_length = 0

        for right in range(n):
            while bitmask & nums[right] != 0:
                bitmask ^= nums[left]
                left += 1

            bitmask |= nums[right]

            max_length = max(max_length, right - left + 1)
        
        return max_length
        