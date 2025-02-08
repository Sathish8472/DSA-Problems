class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        zeros = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                if count > 0:
                    zeros.append(count)
                count = 0

        if count > 0:
            zeros.append(count)


        result = 0
        for i in zeros:
            result += i * (i + 1) // 2

        return result

                

        