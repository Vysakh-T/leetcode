from itertools import combinations
class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        return len([x for x in combinations(arr,3) if( abs(x[0]-x[1])<=a and abs(x[1]-x[2])<=b and abs(x[0]-x[2])<=c)])