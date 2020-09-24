class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if(len(set([i[0] for i in coordinates]))==1 or len(set([i[0] for i in coordinates]))==1):
            return True
        try:
            slope = (coordinates[0][1] - coordinates[1][1])/(coordinates[0][0] - coordinates[1][0])
            for i in range(1,len(coordinates)-1):
                if (coordinates[i][1] - coordinates[i+1][1])/(coordinates[i][0] - coordinates[i+1][0])!=slope:
                    return False
            return True
        except:
            return False