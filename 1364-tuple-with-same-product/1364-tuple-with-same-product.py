class Solution:
    # Optimized Brute Force with Hash Map
    def tupleSameProduct(self, nums: List[int]) -> int: 
        product_map = defaultdict(int)
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_map[product] += 1

        print(product_map)
        count = 0

        for pair_count in product_map.values():
            if pair_count > 1:
                count += pair_count * (pair_count - 1) // 2 * 8

        return count
                


    # Brute Force Approach
    # Time: O(n ^ 4)
    def tupleSameProduct_1(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for l in range(n):
                        if i != j and i != k and i != l and j != k and j != l and k != l:
                            if nums[i] * nums[j] == nums[k] * nums[l]:
                                count += 1
        
        return count