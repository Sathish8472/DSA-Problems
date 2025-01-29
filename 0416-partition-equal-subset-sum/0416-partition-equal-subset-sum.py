class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        arr = nums

        totalSum = sum(arr)

        if totalSum % 2 == 1:
            return False
        else:
            k = totalSum // 2
            prev = [False] * (k + 1)
            prev[0] = True

            if arr[0] <= k:
                prev[arr[0]] = True

            for ind in range(1, n):
                cur = [False] * (k + 1)
                cur[0] = True

                for target in range(1, k + 1):
                    notTaken = prev[target]

                    taken = False

                    if arr[ind] <= target:
                        taken = prev[target - arr[ind]]

                    cur[target] = notTaken or taken

                prev = cur
            return prev[k]
