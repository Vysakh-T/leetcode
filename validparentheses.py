class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for c in s:
            if not stack:
                stack.append(c)
            elif c==')' and stack[-1]=='(':
                stack.pop()
            elif c==']' and stack[-1]=='[':
                stack.pop()
            elif c=='}' and stack[-1]=='{':
                stack.pop()
            else:
                stack.append(c)
        return True if len(stack)==0 else False