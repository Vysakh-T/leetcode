class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        c = 0
        J = list(J)
        S = list(S)
        for a in S:
            if a in J:
                c+=1
        return c