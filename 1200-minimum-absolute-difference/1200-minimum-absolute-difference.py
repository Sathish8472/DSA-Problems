class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_element = min(arr)
        max_element = max(arr)

        shift = -min_element
        line = [0] * (max_element - min_element + 1)
        ans = []

        for num in arr:
            line[num + shift] = 1
        
        min_pair_diff = max_element - min_element
        prev = 0

        for curr in range(1, max_element + shift + 1):
            if line[curr] == 0:
                continue
            
            if curr - prev == min_pair_diff:
                ans.append([prev - shift, curr - shift])
            elif curr - prev < min_pair_diff:
                ans = [(prev - shift, curr - shift)]
                min_pair_diff = curr - prev
            
            prev = curr
        
        return ans