class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        if ruleKey == 'type':
            k=0
        elif ruleKey == 'color':
            k=1
        else:
            k=2
        
        c = 0
        
        for i in items:
               if i[k] == ruleValue:
                    c += 1  
        return c