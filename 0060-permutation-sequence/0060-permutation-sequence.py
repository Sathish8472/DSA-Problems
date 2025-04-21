class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        factorial = math.factorial(n - 1)
        k -= 1 
        result = ""

        for i in range(n - 1, -1, -1):
            index = k // factorial
            result += str(numbers.pop(index))
            if i > 0:
                k %= factorial
                factorial //= i

        return result


    def getPermutation1(self, n: int, k: int) -> str:

        nums = []
        result = []

        for i in range(1, n + 1):
            nums.append(i)
        
        def backtrack(ds):
            if len(ds) == n:
                result.append(ds[:])
                print(ds)

            for i in range(len(nums)):
                if nums[i] in ds:
                    continue
                
                ds.append(nums[i])
                backtrack(ds)
                ds.pop()

        backtrack([])

        arr = result[k - 1]

        ans = ""
        for num in arr:
            ans += str(num)
        return ans
        