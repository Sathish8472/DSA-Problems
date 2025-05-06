class Solution:
    def validStrings(self, n: int) -> List[str]:

        result = []

        self.func("", result, n)

        return result

    
    def func(self, current_string, result, n):
        if len(current_string) == n:
            result.append(current_string)
            return
        
        if not current_string or current_string[-1] == '1':
            self.func(current_string + '0', result, n)
        
        self.func(current_string + '1', result, n)


        
    
