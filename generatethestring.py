class Solution(object):
    def generateTheString(self, n):
        """
        :type n: int
        :rtype: str
        """
        if(n%2==0):
            res = ['x' for i in range(n-1)]
            res.append('y')
            return ''.join(res)
        else:
            return ''.join(['x' for i in range(n)])