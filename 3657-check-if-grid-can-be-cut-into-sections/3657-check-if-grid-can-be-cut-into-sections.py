class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        """
        Determines if it's possible to make two valid vertical or horizontal cuts 
        such that the resulting sections each contain at least one rectangle.
        """
        return self.canMakeTwoValidCuts(rectangles, axis=0) or self.canMakeTwoValidCuts(rectangles, axis=1)

    def canMakeTwoValidCuts(self, rectangles: List[List[int]], axis: int) -> bool:
        """
        Checks if two valid cuts can be made along the given axis (0 for x, 1 for y).
        """
        # Sort rectangles based on their starting coordinate in the chosen axis
        rectangles.sort(key=lambda rect: rect[axis])

        cut_count = 0  # Tracks the number of valid gaps
        max_end_seen = rectangles[0][axis + 2]  # Tracks the furthest ending coordinate seen

        # Iterate through rectangles to find valid gaps
        for i in range(1, len(rectangles)):
            start = rectangles[i][axis]  # Current rectangle's start coordinate
            end = rectangles[i][axis + 2]  # Current rectangle's end coordinate

            # If there's a gap between max_end_seen and the current start, it's a valid cut
            if max_end_seen <= start:
                cut_count += 1  # Found a valid gap

            # Update the furthest end reached so far
            max_end_seen = max(max_end_seen, end)

        # At least 2 valid gaps are needed to create 3 sections
        return cut_count >= 2
