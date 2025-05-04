class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freqmap = {}    
        pairs = 0

        for domino in dominoes:
            normalized_domino = tuple(sorted(domino))
            if normalized_domino in freqmap:
                pairs += freqmap[normalized_domino]
                freqmap[normalized_domino] += 1
            else:
                freqmap[normalized_domino] = 1

        return pairs 


    def numEquivDominoPairs2(self, dominoes: List[List[int]]) -> int:
        counts = {}
        ans = 0
        for domino in dominoes:
            normalized_domino = tuple(sorted(domino))
            if normalized_domino in counts:
                ans += counts[normalized_domino]
                counts[normalized_domino] += 1
            else:
                counts[normalized_domino] = 1
        
        print(counts)
        return ans