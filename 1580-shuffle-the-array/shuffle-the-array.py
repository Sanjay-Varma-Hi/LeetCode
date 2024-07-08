class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        a=[]
        b=[]
        for i in range (0,n):
            a.append(nums[i])
        for j in range (n,n*2):
            b.append(nums[j])
        c = [item for pair in zip(a, b) for item in pair]
        return c
