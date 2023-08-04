# sol 3 (counting 0s)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max_flowers = 0
        zero_streak = 0
        length = len(flowerbed)

        if n == 0:
            return True
        if length == 1 and flowerbed[0] == 0:
            return True

        for i in range(length):
            if flowerbed[i] == 0:
                if i == 0:
                    zero_streak += 2
                elif i == length-1:
                    zero_streak += 2
                    max_flowers += (zero_streak-1)//2
                else:
                    zero_streak += 1
            else:
                if zero_streak > 0:
                    max_flowers += (zero_streak-1)//2
                    zero_streak = 0
        
        return n <= max_flowers



# sol 2 (stop-at-n array traversal by Editorial)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max_flowers = 0
        for i in range(len(flowerbed)):
            left_flower = (i == 0) or (flowerbed[i-1] == 0)
            right_flower = (i == len(flowerbed)-1) or (flowerbed[i+1] == 0)
            if flowerbed[i] == 0 and left_flower and right_flower:
                max_flowers+=1
                flowerbed[i] = 1
                if max_flowers >= n:
                    return True
        
        return n <= max_flowers



# sol 1 (intuitive array traversal)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max_flowers = 0
        length = len(flowerbed)
        if length == 1:
            if flowerbed[0] == 1 and n > 0:
                return False
            else:
                return True
        
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            max_flowers+=1
            flowerbed[0] = 1
        
        for i in range(1, length-1):
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                max_flowers+=1
                flowerbed[i] = 1
        
        if flowerbed[length-1] == 0 and flowerbed[length-2] == 0:
            max_flowers+=1

        return n <= max_flowers