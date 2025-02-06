class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        left_product = 1
        for i, num in enumerate(nums):
            answer[i] = left_product
            left_product *= num

        print("left_product:", left_product)
        print("answer:", answer)
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        print(right_product)
        return answer




    # Brute force
    def productExceptSelf_1(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]

            answer[i] = product

        return answer
