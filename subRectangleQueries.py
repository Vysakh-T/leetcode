class SubrectangleQueries(object):
    
    rectangle = [[]]

    def __init__(self, rectangle):
        """
        :type rectangle: List[List[int]]
        """
        self.rectangle = rectangle

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :type newValue: int
        :rtype: None
        """
        
        r2 = max([row1,row2])+1
        r1 = min([row1,row2])
        c2 = max([col1,col2])+1
        c1 = min([col1,col2])
        for i in range(r1,r2):
            for j in range(c1,c2):
                self.rectangle[i][j] = newValue
        
        
        
    def getValue(self, row, col):
        """
        :type row: int
        :type col: int
        :rtype: int
        """
        return self.rectangle[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)