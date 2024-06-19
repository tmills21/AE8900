class serviceArea:
    def __init__(self, width):
        
        # km
        self.width = width 
        self.area = self.computeArea()

        # per minute
        self.arrivalRate = self.computeArrivalRate()

        # minute
        self.mean = self.computeMean()
        self.variance = self.computeVariance()

    def computeArea(self):

        # assumes 2D square
        return self.width**2
    
    def computeArrivalRate(self):
        
        # assumes 2D square
        return self.width**2/30.0
    
    def computeMean(self):
        
        # assumes 2D square
        return self.width
    
    def computeVariance(self):
        
        # assumes 2D square
        return ( 7 / 6.0 ) * self.width**2
    
    def computeResponseTime(self):
        
        # W in minutes
        factor = self.arrivalRate**2 / ( 2 * self.arrivalRate * ( 1 - self.arrivalRate * self.mean ) )
        return self.mean + factor * self.variance


largeRegion = serviceArea(3)
print(largeRegion.computeResponseTime())