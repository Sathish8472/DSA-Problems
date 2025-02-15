class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_map = defaultdict(list)    # Time: O(1), space: O(1)

        for s in strs:                           # Time: O(n), space: O(1)
            count = [0] * 26                     # Time: O(k), space: O(26)
            for ch in s:                         # Time: O(k), space: O(1)
                count[ord(ch) - ord('a')] += 1   # Time: O(1), space: O(1)
            
            # Use the tuple as the key
            freq_map[tuple(count)].append(s)  # Time: O(1) average for tuple operations, space: O(1)
        return list(freq_map.values())          # Time: O(n), space: O(n * k)



    # Brute force
    # Time : O(n * k log k), Space: O(n * k)
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map : Dict[str, List[str]] = {}    

        for word in strs:                                # Time: O(len(word)), space: O(1)
            sorted_word = "".join(sorted(word))             # Time: O(k log k), space: O(k)
            if sorted_word not in anagram_map:
                anagram_map[sorted_word] = []

            anagram_map[sorted_word].append(word)       # Time: O(1), space: O(1)

        return [group for group in anagram_map.values()]    # Time: O(n), space: O(n * k)
        