class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def _generate_parenthesis(current_string, op, close):

            if len(current_string) == n * 2:
                result.append(current_string)
                print(current_string)
                return

            
            if op < n:
                _generate_parenthesis(current_string + "(", op + 1, close)

            if close < op:
                _generate_parenthesis(current_string + ")", op, close + 1)


        _generate_parenthesis("", 0, 0)

        return result
        
        
    
        