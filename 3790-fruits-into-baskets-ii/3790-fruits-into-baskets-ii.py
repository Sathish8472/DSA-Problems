class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        used = [False] * len(baskets)

        unplaced = 0 

        for i in range(len(fruits)):
            placed = False
            for j in range(len(baskets)):
                if not used[j] and baskets[j] >= fruits[i]:
                    placed = True
                    used[j] = True
                    break

            if not placed:
                unplaced += 1


        return unplaced
        