from itertools import combinations
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        count = 0
        for rate in list(combinations(rating, 3)):
            if(rate[0]<rate[1] and rate[1]<rate[2]):
                count += 1
            elif(rate[2]<rate[1] and rate[1]<rate[0]):
                count += 1
        return count