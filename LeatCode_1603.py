class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small
        
    def addCar(self, carType):
        if carType == 1:
            self.big -= 1
            if self.big < 0:
                return False
            return True

        elif carType == 2:
            self.medium -= 1
            if self.medium < 0:
                return False
            return True
        
        elif carType == 3:
            self.small -= 1
            if self.small < 0:
                return False
            return True