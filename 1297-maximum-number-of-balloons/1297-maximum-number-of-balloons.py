class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_map = {}

        for ch in "balloon":
            if ch not in hash_map:
                hash_map[ch] = 0

        for ch in text:
            if ch in hash_map:
                hash_map[ch] += 1

        print(hash_map)

        count = float('inf')

        for key, value in hash_map.items():
            val = value 

            if key == 'l' or key == 'o':
                val = value // 2

            count = min(count, val)

        return count


    def maxNumberOfBalloons_1(self, text: str) -> int:

        characterExist = True
        target = "balloon"
        count = 0

        while characterExist:
            for ch in target:
                
                if text and text.find(ch) != -1:
                    pos = text.find(ch)
                    text = text[:pos] + text[pos + 1:len(text)]
                    print(text)
                else:
                    characterExist = False
                    print("Break --")
                    return count
                print(ch)

            count += 1
            print("Count", count)
        
        return count
        