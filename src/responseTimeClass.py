import math
import numpy as np

class responseTime:
    def __init__(self, data):
        
        # satellite data
        self.data = data
        self.numSats = len(self.data)
        self.freqLambdaScale = self.numSats / ( 20 * 365.25 ) # calls/day

    def standardResponseTime(self):

        # list all response times in days
        times = [self.data[i][1]/86400 for i in range(self.numSats)]
        timesAvg = np.mean(times)
        timesVar = np.var(times)

        # average response time W in days
        rho = self.freqLambdaScale * timesAvg
        W = timesAvg + ( rho**2 + self.freqLambdaScale**2 * timesVar ) / ( 2 * self.freqLambdaScale * ( 1 - rho ) )
        return W
    
    def getPrioritySplit(self, priAngle):
        priAngle = math.radians(priAngle)
        priSats = []
        nonPriSats = []

        # angle provided defines priority angle in both positive and negative directions
        for i in range(self.numSats):
            angle = self.data[i][0]
            if abs(angle) < abs(priAngle):
                priSats.append(self.data[i])
            else:
                nonPriSats.append(self.data[i])

        return priSats, nonPriSats
    
    def priorityResponseTime(self, priAngle):

        # get fraction of sats in priority and nonpriority area
        priSats, nonPriSats = self.getPrioritySplit(priAngle)
        scale = len(priSats) / self.numSats

        # average response time W in days
        lambda1 = self.freqLambdaScale * scale
        lambda2 = self.freqLambdaScale * ( 1 - scale )

        priTimes = [priSats[i][1]/86400 for i in range(len(priSats))]
        nonPriTimes = [nonPriSats[i][1]/86400 for i in range(len(nonPriSats))]

        ES1 = np.mean(priTimes)
        ES2 = np.mean(nonPriTimes)

        varS1 = np.var(priTimes)
        varS2 = np.var(nonPriTimes)

        ES12 = varS1 + ES1**2
        ES22 = varS2 + ES2**2

        P1 = scale
        P2 = 1 - scale

        W0 = 1 / 2 * ( lambda1 * ES12 + lambda2 * ES22 )

        a1 = lambda1 * ES1
        a2 = a1 + lambda2 * ES2


        Wq1 = W0 / ( 1 - a1 )
        Wq2 = Wq1 / ( 1 - a2 )

        W1 = Wq1 + ES1
        W2 = Wq2 + ES2

        W = P1 * W1 + P2 * W2

        return W