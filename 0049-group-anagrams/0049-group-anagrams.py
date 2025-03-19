class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = set()

        for word in strs:
            words.add("".join(sorted(word)))

        hashmap = {}
        for word in words:
            hashmap[word] = []

        result = []

        for word in strs:
            sorted_word = "".join(sorted(word))
            hashmap[sorted_word].append(word)

        for value in hashmap.values():
            result.append(value)

        return result
