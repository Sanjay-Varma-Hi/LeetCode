class Solution(object):
    def findLHS(self, nums):
        freq = {}
        for x in nums:
            freq[x] = freq.get(x,0)+1
        
        longest = 0
        for x in freq:
            if x+1 in freq:
                longest = max(freq[x]+freq[x+1],longest)
        return longest