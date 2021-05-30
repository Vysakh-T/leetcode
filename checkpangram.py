import string
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(sentence)<26:
            return False
        
        for i in string.ascii_lowercase:
            if i not in sentence:
                return False
            
        return True