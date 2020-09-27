from itertools import chain
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return len(filter(lambda x: x<0,chain.from_iterable(grid)))