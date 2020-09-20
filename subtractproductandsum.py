class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = str(n)
        prod = 1
        su = 0
        for d in digits:
            prod *= int(d)
            su += int(d)
        return(prod-su)