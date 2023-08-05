# sol 2 (by celestial2897, O(n))
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf') 
        for n in nums: 
            if n <= first: 
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
            


# Failed sol 1 (three pointers, O(n^3) too slow)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums) - 1):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[j] and nums[j] < nums[k]:
                        return True
        
        return False