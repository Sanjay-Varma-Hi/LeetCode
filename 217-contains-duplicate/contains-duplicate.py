class Solution(object):
    def containsDuplicate(self, nums):
        a=set(nums)
        if len(nums) == len(a):
            return False
        return True