class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        arr = [start]
        res = arr[0]
        for i in range(1,n):
            arr.append(start+2*i)
            res ^= arr[i]
        return res