class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        t = max(candies)
        for i in range(len(candies)):
            if(candies[i]+extraCandies>=t):
                candies[i]=True
            else:
                candies[i]=False
        return candies