class Solution(object):
    def findLHS(self, nums):
        nums.sort()
        l= 0
        best = 0
        for r in range (len(nums)):
            while nums[r]- nums[l] >1:
                l=l+1
            if nums[r] - nums[l] == 1:
                best = max(best, r-l+1)
        return best