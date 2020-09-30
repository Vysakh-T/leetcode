class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n%2==0:
            res = []
            for i in range(1,int(n/2)+1):
                res.append(i)
                res.append(-i)
        else:
            res = [0]
            for i in range(1,int(n/2)+1):
                res.append(i)
                res.append(-i)
        return res