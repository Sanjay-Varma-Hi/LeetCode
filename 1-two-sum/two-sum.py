class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a=[]
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    a.append(i)
                    a.append(j)
                    return a
        