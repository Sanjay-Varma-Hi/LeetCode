class Solution(object):
    def findNumbers(self, nums):
        res = 0
        for n in nums:
            if 9<n<100 or 999 < n < 10000 or n == 100000:
                res += 1
        return res