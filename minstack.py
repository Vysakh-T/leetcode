class MinStack(object):
    
    s = []
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.insert(0,x)
        

    def pop(self):
        """
        :rtype: None
        """
        self.s=self.s[1:]
        

    def top(self):
        """
        :rtype: int
        """
        return self.s[0]
        
        
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.s)
    
    #Use deque for faster runtimes
