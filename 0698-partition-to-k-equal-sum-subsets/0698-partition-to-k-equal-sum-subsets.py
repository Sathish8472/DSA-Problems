class Solution1:
    def canPartitionKSubsets1(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        hashmap = {}

        def backtrack(start, ds):
            print(ds)
            if len(ds) > 0:
                ds_sum = sum(ds)
                if ds_sum in hashmap:
                    hashmap[ds_sum] += 1
                else:
                    hashmap[ds_sum] = 1

            for i in range(start, n):
                ds.append(nums[i])
                backtrack(i + 1, ds)
                ds.pop()

        backtrack(0, [])
        print(hashmap)

        for val in hashmap.values():
            if val >= k:
                return True

        return False

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        target_sum = total_sum // k
        n = len(nums)
        nums.sort(reverse=True)

        if nums[0] > target_sum:
            return False

        buckets = [0] * k
        visited = [False] * n

        def backtrack(index: int) -> bool:
            if index == n:
                return all(bucket == target_sum for bucket in buckets)

            if visited[index]:
                return backtrack(index + 1)

            num = nums[index]
            for i in range(k):
                if buckets[i] + num <= target_sum:
                    buckets[i] += num
                    visited[index] = True
                    if backtrack(index + 1):
                        return True
                    visited[index] = False
                    buckets[i] -= num
                    # Optimization: If the current bucket is empty, trying to put the current number
                    # in other empty buckets will lead to the same state later. So, break.
                    if buckets[i] == 0:
                        break
            return False

        return backtrack(0)