class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        s = s[::-1]
        for i in range(len(s)):
            res += (ord(s[i])-64)*(26**i)
        return res