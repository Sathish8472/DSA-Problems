class Solution:

    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10 ** 9 + 7
        MAX_N = n + 1
        MAX_VAL = maxValue + 1

        # Step 1: Precompute factorials and inverse factorials
        fact = [1] * MAX_N
        inv_fact = [1] * MAX_N

        for i in range(1, MAX_N):
            fact[i] = fact[i - 1] * i % MOD

        inv_fact[MAX_N - 1] = pow(fact[MAX_N - 1], MOD - 2, MOD)
        for i in range(MAX_N - 2, -1, -1):
            inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b > a or b < 0:
                return 0
            return fact[a] * inv_fact[b] % MOD * inv_fact[a - b] % MOD

        # Step 2: Build the DP table for value counts
        max_len = min(n, 14)  # log2(10^4) ≈ 14 is the longest chain possible
        count = [[0] * (max_len + 1) for _ in range(MAX_VAL)]

        for i in range(1, MAX_VAL):
            count[i][1] = 1

        for length in range(2, max_len + 1):
            for i in range(1, MAX_VAL):
                for j in range(i * 2, MAX_VAL, i):
                    count[j][length] = (count[j][length] + count[i][length - 1]) % MOD

        # Step 3: Calculate final result
        res = 0
        for v in range(1, MAX_VAL):
            for k in range(1, max_len + 1):
                if count[v][k] > 0:
                    res = (res + count[v][k] * comb(n - 1, k - 1)) % MOD

        return res






    # Backtracking - BRute 
    # 10 ^ 4 - Time
    def idealArrays_1(self, n: int, maxValue: int) -> int:
        count = 0
        nums = []

        for i in range(1, maxValue + 1):
            nums.append(i)

        print("nums: ", nums)

        def backtrack(arr):
            nonlocal count
            if len(arr) == n:
                print(arr)
                count += 1
                return

            for i in range(len(nums)):
                if len(arr) > 0:
                    prev = arr[-1]
                    cur = nums[i]
                    if cur % prev != 0:
                        continue
                
                arr.append(nums[i])
                backtrack(arr)
                arr.pop()


        backtrack([])

        return count
        