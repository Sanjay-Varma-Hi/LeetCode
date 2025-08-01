class Solution(object):
    def search(self, nums, target):
        l,r = 0, len(nums)-1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        pi = l

        def bise(left, right):
            while left<=right:
                mid = (left+right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid +1
                else:
                    right = mid -1
            return -1
        res = bise(0,pi-1)
        if res != -1:
            return res
        return bise(pi, len(nums) - 1)
