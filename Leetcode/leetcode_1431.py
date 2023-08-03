# sol 2 (atrocious dict sort)
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        d = dict()
        for i in range(len(candies)):
            d[i] = candies[i]
        
        d = sorted(d.items(), key=lambda x: x[1])
        max = d[-1][1]
        ans = [None] * len(d)

        for i in range(len(d)-1, -1, -1):
            if d[i][1] >= max - extraCandies:
                ans[d[i][0]] = True
            else:
                ans[d[i][0]] = False

        return ans


# sol 1 (find max, then compare)
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = 0
        ans = list()
        for i in range(len(candies)):
            if candies[i] > max:
                max = candies[i]
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max:
                ans.append(True)
            else:
                ans.append(False)

        return ans