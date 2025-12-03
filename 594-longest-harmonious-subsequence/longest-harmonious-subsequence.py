class Solution(object):
    def findLHS(self, nums):
        l = 0
        mp = 0
        nums.sort()
        for r in range (len(nums)):
            while nums[r]-nums[l] > 1:
                l = l+1
            if nums[r] - nums[l] == 1:
                mp = max(mp, r-l+1)
        return mp