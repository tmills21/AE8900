import numpy as np
import matplotlib.pyplot as plt

class serviceAreaSquare:
    def __init__(self, width, inner):

        # calls/hour/km^2
        self.demand = 2

        # km/hr
        self.serviceTimeSpeed = 60
        
        # km
        self.width = width 
        self.inner = inner
        self.area = self.computeArea()
        self.P = self.area / self.width**2

        # per minute
        self.arrivalRate = self.computeArrivalRate()

        # minute
        self.expectation = self.computeExpectation()

        # minute^2
        self.expectationVarSq = self.computeExpectationVarSq()

    def computeArea(self):

        # assumes 2D square
        return self.width**2 - self.inner**2 # km
    
    def computeArrivalRate(self):
        
        # assumes 2D square
        return self.demand * self.area / 60 # per minute
    
    def computeExpectation(self):
        
        # assumes 2D square
        dist = ( self.width - (1 - self.P) * self.inner ) / self.P # km
        return dist * 60 / self.serviceTimeSpeed # min
    
    def computeExpectationVarSq(self):
        
        # assumes 2D square
        expVarSq = ( 7 / 6.0 ) * self.width**2
        innerExpVarSq = ( 7 / 6.0 ) * self.inner**2
        distSq = ( expVarSq  - (1 - self.P ) * innerExpVarSq ) / self.P # km^2
        return distSq * 3600 / self.serviceTimeSpeed**2 # min^2
    

class StandardResponseArea(serviceAreaSquare):
    def __init__(self, width, inner):
        super().__init__(width, inner)

    def computeResponseTime(self):
        
        # W in minutes
        factor = self.arrivalRate / ( 2 * ( 1 - self.arrivalRate * self.expectation ) )
        return self.expectation + factor * self.expectationVarSq
    
class PriorityResponseArea(serviceAreaSquare):

    # assumes only two regions
    def __init__(self, width, inner):
        super().__init__(width, inner)
        self.containedArea = serviceAreaSquare(inner, 0)

    def computeResponseTime(self):
        
        # W in minutes
        lambda1 = self.containedArea.arrivalRate
        lambda2 = self.arrivalRate

        ES1 = self.containedArea.expectation
        ES2 = self.expectation

        ES12 = self.containedArea.expectationVarSq
        ES22 = self.expectationVarSq

        P2 = self.P
        P1 = 1 - P2

        W0 = 1 / 2 * ( lambda1 * ES12 + lambda2 * ES22 )

        a1 = lambda1 * ES1
        a2 = a1 + lambda2 * ES2


        Wq1 = W0 / ( 1 - a1 )
        Wq2 = Wq1 / ( 1 - a2 )

        W1 = Wq1 + ES1
        W2 = Wq2 + ES2

        W = P1 * W1 + P2 * W2 # min

        return W
    

if __name__ == "__main__":
    outer = 3

    region = StandardResponseArea(3, 0)
    standardResponse = region.computeResponseTime()

    # get priority queue times 
    buffer = 0.001
    xs = np.linspace(buffer, outer - buffer, 50)
    priTimes = []
    for i in range(len(xs)):
        region = PriorityResponseArea(outer, xs[i])
        priTimes.append(region.computeResponseTime())

    min_index = priTimes.index(min(priTimes))
    print('min time = ' + str(min(priTimes)) + " at side length = " + str(xs[min_index]))
    print(str(xs[min_index]/outer) + ' of the way')

    plt.figure(figsize=(10, 6))
    plt.plot(xs, priTimes, label='Priority Queue')
    plt.plot([0, 3], [standardResponse] * 2, label='Standard Queue')
    plt.title('Average Response Times for Queueing Types')
    plt.xlabel('Priority Area Side Length')
    plt.ylabel('Average Response Time (minutes)')
    plt.legend()
    plt.grid(True)
    plt.show()