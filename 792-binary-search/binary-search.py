class Solution(object):
    def search(self, nums, target):
        for i in range (0,len(nums)):
            if nums[i]==target:
                return i
        return -1
        # i=0
        # n = len(nums)
        # low = 0
        # high = n

        # while low<=high:
        #     mid = low+(high-low)//2
        #     if nums[mid] == target:
        #         return mid