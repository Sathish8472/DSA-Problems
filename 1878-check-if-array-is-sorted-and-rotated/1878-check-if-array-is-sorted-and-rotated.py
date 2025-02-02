class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        orgNumbers = sorted(nums)
        print(orgNumbers)

        for i in range(n):
            rotated = orgNumbers[i:] + orgNumbers[:i]
            print("i: ", i);
            print("Orgin: ", orgNumbers)
            print("Org i:", orgNumbers[i:])
            print("Org :i", orgNumbers[:i])
            if rotated == nums:
                return True

        return False



    
        

        