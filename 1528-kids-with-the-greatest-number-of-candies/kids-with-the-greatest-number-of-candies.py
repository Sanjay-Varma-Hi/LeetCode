class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        x=max(candies)
        c=[]
        for i in candies:
            if i+extraCandies >= x:
                c.append(True)
            else:
                c.append(False)
        return c
