from re import findall
class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        o = 0
        z = 0
        try:
            o = len(max(findall("11*",s)))
            z = len(max(findall("00*",s)))
        except:
            None
        return True if o>z else False