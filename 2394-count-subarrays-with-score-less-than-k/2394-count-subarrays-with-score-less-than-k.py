class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)
        sumV = 0
        counter = 0
        left = 0

        for right in range(n):
            sumV += nums[right]

            while sumV * (right - left + 1) >= k:
                sumV -= nums[left]
                left += 1

            count += (right - left + 1)

        return count


    def countSubarrays1(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        sumV = 0
        for i in range(n):
            counter = 0
            sumV = 0
            for j in range(i, n):
                sumV += nums[j]
                counter += 1

                if sumV * counter < k:
                    count += 1

        return count
        