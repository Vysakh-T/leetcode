class Solution(object):
    def fib(self, n, memo = dict()):
        """
        :type n: int
        :rtype: int
        """
        if(memo.get(n)!=None):
            return memo[n]
        if n<=1:
            return n
        else:
            memo[n] = self.fib(n-1,memo) + self.fib(n-2,memo)
            return memo[n]