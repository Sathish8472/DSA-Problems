class Solution:

    def countBits(self, n : int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)  # Right shift + last bit check
        
        return ans

        

    # Brute
    # time: O(n log n), Space: O(N)
    def countBits_1(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        def getCount(num):
            count = 0
            while num > 0:
                count += 1
                num = num & (num - 1)
            return count

        for i in range(len(ans)):
            count = getCount(i)
            ans[i] = count

        return ans
