class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        pos_count = 0
        neg_count = 0

        for num in nums:
            if num < 0:
                neg_count += 1
            elif num > 0:
                pos_count += 1
        
        print(f'pos: {pos_count}, neg: {neg_count}')
        return max(pos_count, neg_count)

        