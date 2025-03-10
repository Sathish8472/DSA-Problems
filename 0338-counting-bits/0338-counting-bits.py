class Solution:
    def countBits(self, n: int) -> List[int]:
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

        print(ans)
        return ans
