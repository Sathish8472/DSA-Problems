class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        top_counts = {}
        bottom_counts = {}

        for i in range(n):
            top_counts[tops[i]] = top_counts.get(tops[i], 0) + 1
            bottom_counts[bottoms[i]] = bottom_counts.get(bottoms[i], 0) + 1

        top_target = None
        max_top_count = -1
        for num, count in top_counts.items():
            if count >= max_top_count:
                max_top_count = count
                top_target = num

        bottom_target = None
        max_bottom_count = -1
        for num, count in bottom_counts.items():
            if count >= max_bottom_count:
                max_bottom_count = count
                bottom_target = num

        rotations = 0
        print(f"target: ", top_target)
        if max_top_count >= max_bottom_count:
            print(f"max_top_count: ", max_top_count)

            rotations = self._calculate_rotations(top_target, tops, bottoms)
        else:
            print(f"max_bottom_count: ", max_bottom_count)
            rotations = self._calculate_rotations(bottom_target, bottoms, tops)

        return rotations

    def _calculate_rotations(
        self, target: int, source: List[int], dest: List[int]
    ) -> int:
        rotations = 0
        n = len(source)

        for i in range(n):
            if source[i] != target and dest[i] == target:
                rotations += 1
            elif source[i] == target:
                continue
            else:
                return -1

        return rotations