class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap = {}

        total_pairs = len(nums) // 2
        pair_count = 0

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        print(hashmap)

        pair_count += sum(value // 2 for value in hashmap.values())
        if pair_count == total_pairs:
            return True

        return False
