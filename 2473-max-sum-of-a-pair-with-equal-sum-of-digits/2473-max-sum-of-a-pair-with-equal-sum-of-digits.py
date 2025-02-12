class Solution:

    def maximumSum(self, nums: List[int]) -> int:

        def digitSum(num: int) -> int:
            total = 0
            while num > 0:
                total += num % 10
                num = num // 10
            
            return total
        
        digit_sum_map = {}
        for num in nums:
            d_sum = digitSum(num)
            if d_sum not in digit_sum_map:
                digit_sum_map[d_sum] = [num]
            else:
                digit_sum_map[d_sum].append(num)
                digit_sum_map[d_sum] = sorted(digit_sum_map[d_sum], reverse = True)[:2]


        max_sum = -1
        for values in digit_sum_map.values():
            if len(values) >= 2:
                max_sum = max(max_sum, values[0] + values[1])

        return max_sum




    # Brute Force 
    def maximumSum_1(self, nums: List[int]) -> int:
        
        def digitSum(num: int) -> int:
            total = 0
            while num > 0:
                digit += num % 10
                num = num // 10
            
            return total
        
        n = len(nums)
        max_sum = -1
        for i in range(n):
            for j in range(i + 1, n):
                if digitSum(nums[i]) == digitSum(nums[j]):
                    max_sum = max(max_sum, nums[i] + nums[j])
                
        return max_sum;

        
        