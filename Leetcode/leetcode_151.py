# sol 3 (no split - Credit: discregionals)
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        temp = ""
        for c in s:
            if c != " ":
                temp += c 
            elif temp != "":
                res.append(temp)
                temp = ""
        if temp != "":
            res.append(temp)
        return " ".join(res[::-1])



# sol 2 (one liner)
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])



# sol 1 (reverse iterative)
class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        reversed_s_list = []
        for i in range(len(s_list)-1, -1, -1):
            reversed_s_list.append(s_list[i])
        return ' '.join(reversed_s_list)