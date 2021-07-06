class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0
        return len(haystack.split(needle)[0]) if len(haystack.split(needle))>1 else -1

        #Tried to solve this without using the find or index function; Using some sort of iteration with pointers is the required solution though