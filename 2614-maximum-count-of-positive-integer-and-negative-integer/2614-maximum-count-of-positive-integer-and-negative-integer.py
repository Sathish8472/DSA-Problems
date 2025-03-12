class Solution:


    def maximumCount(self, nums: List[int]) -> int:
        if not nums:
            return 0

        neg_count = bisect.bisect_left(nums, 0)
        pos_count = bisect.bisect_right(nums, 0)

        pos_count = len(nums) - pos_count
        print(f"pos: {pos_count}, neg: {neg_count}")
        return max(pos_count, neg_count)



    # Two pointer technique
    # time: O(N), Space: O(1)
    # This technique takes time O(n / 2), but in Big If Notation its will be O(N)
    def maximumCount1(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left, right = 0, len(nums) - 1
        neg, pos = 0, 0

        while left <= right:
            if nums[left] < 0:
                neg += 1
            elif nums[left] > 0:
                pos += 1

            if left != right:
                if nums[right] < 0:
                    neg += 1
                if nums[right] > 0:
                    pos += 1

            left += 1
            right -= 1

        print(f"pos: {pos}, neg: {neg}")
        return max(pos, neg)

    def maximumCount1(self, nums: List[int]) -> int:
        if not nums:
            return 0

        pos_count, neg_count = 0, 0

        for num in nums:
            if num < 0:
                neg_count += 1
            elif num > 0:
                pos_count += 1

        print(f"pos: {pos_count}, neg: {neg_count}")
        return max(pos_count, neg_count)

    def maximumCount_1(self, nums: List[int]) -> int:

        pos_count = sum(1 for num in nums if num > 0)
        neg_count = sum(1 for num in nums if num < 0)

        return max(pos_count, neg_count)
