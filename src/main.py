from TLEdataClass import *
from serviceSatelliteClass import *
from performSimpleServiceClass import *
from responseTimeClass import *
from plotting import *

import numpy as np
import matplotlib.pyplot as plt

def generateOnce(sats, M):
    servicer = serviceSatellite(newestYear, newestDay, M)

    # initialize variables for service
    numSats = len(sats.satellites)
    serviceTimes = []
    service = performService(True, True, True)

    # iterate over all satellites
    for i in range(numSats):

        # simplify the orbit to circular GEO
        target = service.simplifyOrbit(sats.satellites[i])

        # get angle between servicer and target
        theta = service.getPhaseAngle(servicer.serviceSat, target)

        # compute time for there and back
        time = service.computeTimeHohmann(theta)
        serviceTimes.append((theta, time))

    # make object to get priority and non priority data from
    response = responseTime(serviceTimes)
    sideLength = 3

    # get response time with and without priority queue 
    [xsOrbital, priTimesOrbital, standardTimeOrbital] = computeVaryingPriorityOrbital(response, 0.1)
    # [xsSquare, priTimesSquare, standardTimeSquare] = computeVaryingPrioritySquare(sideLength, 0.001)

    # plot the data
    plotVaryingPriorityOrbital(xsOrbital, priTimesOrbital, standardTimeOrbital)
    # plotVaryingPrioritySquare(xsSquare, priTimesSquare, standardTimeSquare, sideLength)
    plt.show()

def generateMany(sats):

    # initialize variables for service
    numSats = len(sats.satellites)
    service = performService(True, True, True)

    servicerMeanAnomalies = np.linspace(0, 359, 360)

    minResponseTimes = []
    minPriorityAngle = []

    for i in range(len(servicerMeanAnomalies)):
        serviceTimes = []
        servicer = serviceSatellite(newestYear, newestDay, servicerMeanAnomalies[i])

        # iterate over all satellites
        for j in range(numSats):

            # simplify the orbit to circular GEO
            target = service.simplifyOrbit(sats.satellites[j])

            # get angle between servicer and target
            theta = service.getPhaseAngle(servicer.serviceSat, target)

            # compute time for there and back
            time = service.computeTimeHohmann(theta)
            serviceTimes.append((theta, time))

        # make object to get priority and non priority data from
        response = responseTime(serviceTimes)

        # get response time with and without priority queue 
        [xsOrbital, priTimesOrbital, standardTimeOrbital] = computeVaryingPriorityOrbital(response, 0.5)

        min_index = priTimesOrbital.index(min(priTimesOrbital))
        minResponseTimes.append(min(priTimesOrbital))
        minPriorityAngle.append(xsOrbital[min_index])

    plotVaryingPriorityandAnomalyOrbital(servicerMeanAnomalies, minResponseTimes)
    plotVaryingPriorityandAnomalyOrbital(servicerMeanAnomalies, minPriorityAngle)

if __name__ == "__main__":

    # read in all satellites and propogate them in time to most recent one
    filename = "./data/geo.txt"
    sats = TLEdata(filename)
    [(newestYear, newestDay), (oldestYear, oldestYear)] = sats.getOldestAndNewest()
    sats.propogateToSameTime(newestYear, newestDay)

    # generateOnce(sats, 350)
    generateMany(sats)

    plt.show()