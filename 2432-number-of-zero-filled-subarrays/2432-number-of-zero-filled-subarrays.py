class Solution:

    # Single pass count
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = total = 0

        for num in nums:
            if num == 0:
                count += 1
                total += count
            else:
                count = 0

        return total



    # List to store zero counts
    def zeroFilledSubarray_1(self, nums: List[int]) -> int:
        zeros = []
        count = 0
        for num in nums:
            if num == 0:
                count += 1
            else:
                if count > 0:
                    zeros.append(count)
                count = 0

        if count > 0:
            zeros.append(count)

        return sum(i * (i + 1) // 2 for i in zeros)