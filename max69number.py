class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        try:
            return int(str(num).split('6',1)[0]+'9'+str(num).split('6',1)[1])
        except:
            return num