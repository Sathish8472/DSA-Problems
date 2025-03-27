class Solution:
    def minimumIndex(self, nums: List[int]) -> int:

        candidate = count = 0

        for num in nums:
            if count == 0:
                candidate = num

            count += 1 if candidate == num else -1

        total_count = sum(1 for num in nums if candidate == num)

        left_count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] == candidate:
                left_count += 1

            right_count = total_count - left_count
            left_size = i + 1
            right_size = n - left_size

            if left_count * 2 > left_size and right_count * 2 > right_size:
                return i

        return -1
