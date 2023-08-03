# sol 3 (gcd method)
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if ''.join(str1, str2) == ''.join(str2, str1):
            return str1[:math.gcd(len(str1),len(str2))]
        return ""
    


# sol 3 with tuples
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        tup1 = (str1, str2)
        tup2 = (str2, str1)
        if ''.join(tup1) == ''.join(tup2):
            return str1[:math.gcd(len(str1),len(str2))]
        return ""



# sol based on Algorithms Casts' sol
# skips the list() in sol 1/2 since it's unnecessary
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        if n1 > n2:
            return self.gcdOfStrings(str2, str1)
        
        for L in range(n1, 0, -1):
            if n1 % L == 0 and n2 % L == 0:
                if str1[:L] * (n1 // L) == str1 and str1[:L] * (n2 // L) == str2:
                    return str1[:L]
        
        return ""



# sol 2 (brute force, min)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        subs = list()
        largest_str = ""
        if len(str2) < len(str1):
            return gcdOfStrings(str2, str1)

        for i in range(1, len(str1)+1):
            if str1 == str1[0:i] * int(len(str1) / i):
                subs.append(str1[0:i])

        if len(subs) == 0:
            return ""
        
        for i in range(len(subs)):
            if str2 == subs[i] * int(len(str2) / len(subs[i])):
                largest_str = subs[i]
        return largest_str
    


# sol 1 (brute force)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        subs = list()
        largest_str = ""

        for i in range(1, len(str1)+1):
            if str1 == str1[0:i] * int(len(str1) / i):
                subs.append(str1[0:i])

        if len(subs) == 0:
            return ""
        
        for i in range(len(subs)):
            if str2 == subs[i] * int(len(str2) / len(subs[i])):
                largest_str = subs[i]
        return largest_str