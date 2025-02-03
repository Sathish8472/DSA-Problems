# Optimized solution: Single iteration

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_length = inc_length = dec_length = 1
        n = len(nums)

        for i in range(n - 1):
            if nums[i + 1] > nums[i]:  # Increasing
                inc_length += 1
                dec_length = 1
            elif nums[i + 1] < nums[i]:
                dec_length += 1
                inc_length = 1
            else:
                inc_length = dec_length = 1

            max_length = max(max_length, inc_length, dec_length)
                
        return max_length


# Brute force approach
# Time: O(n ^ 2)

class Solution_1:
    def longestMonotonicSubarray_1(self, nums: List[int]) -> int:
        max_length = 1
        n = len(nums)
        
        # Increasing sub array
        for start in range(n):
            current_length = 1
            for pos in range(start + 1, n):
                if nums[pos] > nums[pos - 1]:
                    current_length += 1
                else:
                    break

            max_length = max(max_length, current_length)

        # Decreasing sub array
        for start in range(n):
            current_length = 1
            for pos in range(start + 1, n):
                if nums[pos] < nums[pos - 1]:
                    current_length += 1
                else:
                    break

            max_length = max(max_length, current_length)

        return max_length

