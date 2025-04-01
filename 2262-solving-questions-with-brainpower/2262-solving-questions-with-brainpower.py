class Solution:

    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_question = i + brainpower + 1

            solve = points + (dp[next_question] if next_question < n else 0)

            skip = dp[i + 1]

            dp[i] = max(solve, skip)

        return dp[0]




    # My approach went wrong, but still its mine
    def mostPoints_1(self, questions: List[List[int]]) -> int:
        max_points = 0

        def backtrack(start):
            points = 0
            counter = 0

            for i in range(start, len(questions)):
                [point, brain_power] = questions[i]

                if counter == 0:
                    counter = brain_power
                    points += point

                counter -= 1
                print("counter: ", counter)
                print("points: ", points)

            return points

        for i in range(len(questions)):
            points = backtrack(i)
            max_points = max(max_points, points)

        return max_points
