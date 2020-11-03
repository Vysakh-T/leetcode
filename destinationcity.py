class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        s1 = set()
        s2 = set()
        for i in paths:
            s1.add(i[0])
            s2.add(i[0])
            s2.add(i[1])
        return (s2-s1).pop()