class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor_sum = 0
        for num in derived:
            xor_sum ^= num
        
        # if XOR sum is 0, a valid original array exists because of circular dependency
        return xor_sum == 0
        