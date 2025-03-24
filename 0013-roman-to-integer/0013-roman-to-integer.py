class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        result = 0
        prev_val = float('inf')
        curr_val = 0
        for ch in s:
            curr_val = hashmap[ch]

            print("curr_Val: ", curr_val)
            if curr_val > prev_val:
                
                result -= prev_val
                result += curr_val - prev_val
                print("inside result: ", result)
            else:
                result += curr_val
            prev_val = curr_val
            print("result: ", result)

        return result

        
