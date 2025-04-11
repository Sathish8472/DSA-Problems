class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:

        return self._solve(questions, 0)
        
    def _solve(self, questions, ind) -> int:
        if ind >= len(questions):
            return 0
        
        quest = questions[ind]
        print("Question: ", quest)

        solve = quest[0] + self._solve(questions, ind + quest[1] + 1)

        skip = 0 + self._solve(questions, ind + 1)

        return max(solve, skip)
        