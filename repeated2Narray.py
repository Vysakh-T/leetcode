class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        N = int(len(A)/2)
        l=A[N-2:N+2]
        for i in range(4):
            if l[i] in l[0:i]+l[i+1:]:
                return l[i]