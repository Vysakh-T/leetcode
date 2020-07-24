class Solution(object):
    def reverse(self,x):
        """
        :type x: int
        :rtype: int
        """
 
        x = str(x)[::-1]
        x = -int(x[:-1]) if x[-1]=='-' else int(x)
        if abs(x) > ((2**31)-1):
            return 0
        return x


