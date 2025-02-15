class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = {}

        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str not in freq_map:
                freq_map[sorted_str] = []

            freq_map[sorted_str].append(s)

        return [value for value in freq_map.values()]
        