from TLEdataClass import *

import numpy as np
np.random.seed(100)

class serviceRequest:
    def __init__(self, frequency, timeSpan, sats):
        self.frequency = frequency # lambda, requests/year
        self.timeSpan = timeSpan # years
        self.sats = sats
        self.requestTimes = self.getRequestTimes() # times in seconds
        self.requestSats = self.getRequestSats()

    def getRequestTimes(self):
        time = 0
        requestTimes = []
        while time < self.timeSpan:
            timeInterval = np.random.exponential(1 / self.frequency)
            time += timeInterval
            requestTimes.append(time)

        if requestTimes[-1] > self.timeSpan:
            requestTimes = requestTimes[:-1]

        secondsPerYear = 31557600
        requestTimes = [i * secondsPerYear for i in requestTimes]
        return requestTimes
    
    def getRequestSats(self):
        numRequests = len(self.requestTimes)
        numSats = len(self.sats.satellites)
        random_integers = np.random.randint(1, numSats, numRequests)
        return random_integers
    
if __name__ == "__main__":
    filename = "./data/geoSmall.txt"
    sats = TLEdata(filename)

    test = serviceRequest(0.5, 100, sats)
    print(test.requestTimes)
    print(test.requestSats)