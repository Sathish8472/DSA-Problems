class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        right_sum = 0
        left_sum = 0
        for i in range(n):
            left_sum += nums[i]
        
        print(left_sum)

        for j in range(n - 1, 0, -1):
            right_sum += nums[j]
            left_sum -= nums[j]

            if (left_sum - right_sum) % 2 == 0:
                count += 1

        return count


    def countPartitions_1(self, nums: List[int]) -> int:

        n = len(nums)

        count = 0
        left_sum = 0

        for i in range(n - 1):
            left_sum += nums[i]
            right_sum = 0
            for j in range(i + 1, n):
                right_sum += nums[j]

            if (left_sum - right_sum) % 2 == 0:
                count += 1

        return count
