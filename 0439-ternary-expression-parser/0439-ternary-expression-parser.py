class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []

        i = len(expression) - 1

        while i >= 0:
            ch = expression[i]

            if stack and stack[-1] == '?':
                stack.pop()      # remove ?
                true_val = stack.pop()
                stack.pop()      # remove :
                false_val = stack.pop()

                if ch == 'T':
                    stack.append(true_val)
                else:
                    stack.append(false_val)
                
                i -= 1
            else:
                stack.append(ch)
                i -= 1
        
        return stack[-1]