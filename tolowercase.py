class Solution(object):
    def toLowerCase(self, string):
        """
        :type str: str
        :rtype: str
        """
        for i,s in enumerate(string):
            if ord(s) in range(65,91):
                string = string[:i]+chr(ord(s)+32)+string[i+1:]
        return string