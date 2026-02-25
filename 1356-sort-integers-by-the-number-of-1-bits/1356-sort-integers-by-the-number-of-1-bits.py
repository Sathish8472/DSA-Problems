class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda x: (bin(x).count('1'), x))
        

        
    def sortByBits3(self, arr: List[int]) -> List[int]:
        def bitCount(n):
            return bin(n).count('1')

        return sorted(arr, key = lambda x: (bitCount(x), x))

    
    # Built-in
    def sortByBits2(self, arr: List[int]) -> List[int]:
        def bitCount(n):
            return bin(n).count('1')

        return sorted(arr, key = lambda x: (x.bit_count(), x))


    
    # Manually counting
    def sortByBits1(self, arr: List[int]) -> List[int]:

        def getBitCount(n):
            count = 0
            while n > 0:
                if n & 1 == 1:
                    count += 1
                n = n >> 1

            return count

        return sorted(arr, key = lambda x: (getBitCount(x), x))
