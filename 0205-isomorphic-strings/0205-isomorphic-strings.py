class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Use two dictionaries to store mappings
        s_to_t = {}
        t_to_s = {}
        
        for char_s, char_t in zip(s, t):
            # Check mapping for s -> t
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t
            
            # Check mapping for t -> s (to ensure reverse mapping is also consistent)
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True



    def isIsomorphic_1 (self, s: str, t: str) -> bool:
        sFreq_map = defaultdict(int)

        for ch in s:
            if ch in sFreq_map:
                sFreq_map[ch] += 1
            else:
                sFreq_map[ch] = 1

        print(sFreq_map)

        tFreq_map = defaultdict(int)
        for ch in t:
            if ch in tFreq_map:
                tFreq_map[ch] += 1
            else:
                tFreq_map[ch] = 1

        print(tFreq_map)
        print("---")
        sFreq = []
        for key, value in sFreq_map.items():
            sFreq.append(value)

        tFreq = []
        for key, value in tFreq_map.items():
            tFreq.append(value)

        if sFreq == tFreq:
            return True
        return False
