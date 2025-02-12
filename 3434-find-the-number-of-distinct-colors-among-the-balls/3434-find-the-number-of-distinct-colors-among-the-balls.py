class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}  # Stores the current color of each ball
        color_count = defaultdict(int)  # Counts how many balls have each color
        result = []

        for ball, color in queries:
            # If the ball already has a color, decrease the count for that color
            if ball in ball_colors:
                old_color = ball_colors[ball]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:  # Remove the color if no balls have it
                    del color_count[old_color]

            # Update the ball's color and increase the count for the new color
            ball_colors[ball] = color
            color_count[color] += 1

            # The number of distinct colors is the number of keys in color_count
            result.append(len(color_count))

        return result
