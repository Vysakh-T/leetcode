class ParkingSystem(object):
    space = {1:0,2:0,3:0}

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.space[1] = big
        self.space[2] = medium
        self.space[3] = small
        
        

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.space[carType]==0:
            return False
        else:
            self.space[carType]-=1
            return True
            
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)