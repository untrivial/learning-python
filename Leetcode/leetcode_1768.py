# sol 2 (two pointers)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        ans=[]
        for x in range(max(len(word1), len(word2))):
            if i < len(word1):
                ans += word1[i]
                i += 1
            if j < len(word2):
                ans += word2[j]
                j += 1
        return ''.join(ans)


# sol 1 (one pointer)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        for i in range ( max ( len(word1), len(word2) )):  
            if i < len(word1):
                ans+=word1[i]
            if i < len(word2):
                ans+=word2[i]
        return ''.join(ans)