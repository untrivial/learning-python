# sol 2 (left/right pointers)
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s_list = list(s)
        i = 0
        j = len(s_list) - 1

        while i < j:
            if s_list[i] in vowels:
                if s_list[j] in vowels:
                    temp = s_list[i]
                    s_list[i] = s_list[j]
                    s_list[j] = temp
                    j-=1
                    i+=1
                else:
                    j-=1
            else:
                i+=1
        
        return ''.join(s_list)

# sol 2.1 (easier to read - left/right pointers)
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s_list = list(s)
        i = 0
        j = len(s_list) - 1

        while i < j:
            while s_list[i] not in vowels and i < j:
                i+=1
            while s_list[j] not in vowels and i < j:
                j-=1
            if i < j:
                temp = s_list[i]
                s_list[i] = s_list[j]
                s_list[j] = temp
                i+=1
                j-=1

        return ''.join(s_list)

# sol 1 (str -> list, stack of vowels)
class Solution:
    def reverseVowels(self, s: str) -> str:
        s_list = list(s)
        vowels = []
        for i in range(len(s_list)):
            if s_list[i] in 'aeiouAEIOU':
                vowels.append(s_list[i])
                s_list[i] = 0
        
        for i in range(len(s_list)):
            if s_list[i] == 0:
                s_list[i] = vowels.pop()
        
        return ''.join(s_list)