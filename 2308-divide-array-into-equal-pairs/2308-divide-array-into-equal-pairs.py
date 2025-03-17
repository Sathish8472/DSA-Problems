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

        for count in hashmap.values():
            if count % 2 != 0:
                return False

        return True

    def divideArray2(self, nums: List[int]) -> bool:
        count = Counter(nums)

        print(count)

        for value in count.values():
            if value % 2 != 0:
                return False

        return True
