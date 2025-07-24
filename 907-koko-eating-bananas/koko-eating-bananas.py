class Solution(object):
    def minEatingSpeed(self, piles, h):
        l = 1
        r = max(piles)
        while l<r:
            mid = (l+r)//2
            tt = 0
            for p in piles:
                tt += (p+mid-1)//mid

            if tt<=h:
                r = mid
            else:
                l= mid+1
        return r