class Solution(object):
    def climbStairs(self, n, memo = {}):
        """
        :type n: int
        :rtype: int
        """
        if memo.get(n)!=None:
            return memo[n]
        if n == 1:
            return 1
        elif n==2:
            return 2
        else:
            memo[n] = self.climbStairs(n-1,memo) + self.climbStairs(n-2,memo)
            return memo[n]
