class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0]
        def rec(i,n):
            if(i==n+1):
                return
            if(i==n):
                count[0]=count[0]+1
                return
            rec(i+1,n)
            rec(i+2,n)
        rec(0,n)
        return count[0]
