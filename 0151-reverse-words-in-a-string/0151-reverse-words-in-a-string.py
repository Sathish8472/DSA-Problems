class Solution:
    def reverseWords(self, s: str) -> str:
        result = s.split(" ")

        r = []
        for i in range(len(result)):
            if result[i].strip() != "":
                r.append(result[i].strip())

        r.reverse()
        print(result)
        
        return " ".join(r)