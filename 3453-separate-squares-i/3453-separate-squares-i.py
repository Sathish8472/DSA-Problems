class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        def area_below(h: float) -> float:
            total = 0.0
            for x, y, l in squares:
                top = y + l
                if h <= y:
                    continue  # Entire square is above h
                elif h >= top:
                    total += l * l  # Entire square is below h
                else:
                    height = h - y
                    total += l * height  # Partial contribution
            return total

        # Total area
        total_area = sum(l * l for _, _, l in squares)
        target = total_area / 2

        # Binary search range: from min y to max y + l
        lo = min(y for _, y, _ in squares)
        hi = max(y + l for _, y, l in squares)

        for _ in range(100):  # Enough iterations to reach precision
            mid = (lo + hi) / 2
            if area_below(mid) < target:
                lo = mid
            else:
                hi = mid

        return lo
