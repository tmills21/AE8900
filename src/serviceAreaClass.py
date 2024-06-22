class serviceArea:
    def __init__(self, width, inner):
        
        # km
        self.width = width 
        self.inner = inner
        self.area = self.computeArea()
        self.P = self.area / self.width**2

        # per minute
        self.arrivalRate = self.computeArrivalRate()

        # minute
        self.mean = self.computeMean()
        self.variance = self.computeVariance()

    def computeArea(self):

        # assumes 2D square
        return self.width**2 - self.inner**2
    
    def computeArrivalRate(self):
        
        # assumes 2D square
        return self.area/30.0
    
    def computeMean(self):
        
        # assumes 2D square
        return ( self.width - (1 - self.P) * self.inner ) / self.P
    
    def computeVariance(self):
        
        # assumes 2D square
        totalVar = ( 7 / 6.0 ) * self.width**2
        innerVar = ( 7 / 6.0 ) * self.inner**2
        return ( totalVar  - (1 - self.P ) * innerVar ) / self.P
    
    def computeResponseTime(self):
        
        # W in minutes
        factor = self.arrivalRate / ( 2 * ( 1 - self.arrivalRate * self.mean ) )
        return self.mean + factor * self.variance

if __name__ == "__main__":
    largeRegion = serviceArea(3, 2)
    print(largeRegion.computeArrivalRate())