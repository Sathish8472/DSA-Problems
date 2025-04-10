class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0

        if n == 1:
            return nums[0]

        temp1 = []
        temp2 = []

        for i in range(n):
            if i != n - 1:
                temp1.append(nums[i])

            if i != 0:
                temp2.append(nums[i])

        ans1 = self._helper(temp1)
        ans2 = self._helper(temp2)

        return max(ans1, ans2)

    def _helper(self, nums: List[int]):

        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        prev2 = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, n):
            rob = nums[i] + prev2
            no_rob = prev
            curi = max(rob, no_rob)

            prev2 = prev
            prev = curi

        return prev
