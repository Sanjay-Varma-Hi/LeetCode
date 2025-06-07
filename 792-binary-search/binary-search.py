class Solution(object):
    def search(self, nums, target):
        # for i in range (0,len(nums)):
        #     if nums[i]==target:
        #         return i
        # return -1
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r)//2

            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid
        return -1
