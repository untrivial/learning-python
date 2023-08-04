# You must write an algorithm that runs in O(n) time and without using the division operation.

# sol 2 (single pass using prefix/suffix sum, Credit: sudesh_pawar)
# each iteration multiples the prefix to one end, and the suffix to the mirror/other end
# since both pointers traverse the whole list, all prefixes and suffixes will be multiplied
# essentially separating the prefix and suffix portions, so that 2 pointers may be used
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)



# Failed sol 1 (intuitive multiplication, O(n^2))
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    ans[i] = ans[i] * nums[j]
        return ans