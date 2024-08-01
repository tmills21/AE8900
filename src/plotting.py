from serviceAreaSquareClass import *

import matplotlib.pyplot as plt
import numpy as np

def computeVaryingPriorityOrbital(response, buffer):

    # response time without priority queue
    standardTime = response.standardResponseTime()

    # response with prioity queue
    xs = np.linspace(buffer, 180 - buffer, 500)
    priTimes = []
    for i in range(len(xs)):
        priTimes.append(response.priorityResponseTime(xs[i]))

    # get smallest wait time from priority queue
    min_index = priTimes.index(min(priTimes))
    print('min time = ' + str(min(priTimes)) + " at angle = " + str(xs[min_index]))
    print(str(xs[min_index]/180) + ' of the way')

    return [xs, priTimes, standardTime]


def plotVaryingPriorityOrbital(xs, priTimes, standardTime):
    plt.figure(figsize=(10, 6))
    plt.plot(xs, priTimes, label='Priority Queue')
    plt.plot([0, 180], [standardTime] * 2, label='Standard Queue')
    plt.title('Average Response Times for Queueing Types')
    plt.xlabel('Half Angle of Priority (degrees)')
    plt.ylabel('Average Response Time (days)')
    plt.legend()
    plt.grid(True)
    return plt

def plotVaryingPriorityandAnomalyOrbital(xs, priTimes):
    plt.figure(figsize=(10, 6))
    plt.plot(xs, priTimes, label='Priority Queue')
    plt.title('Change in Minimum Average Response Rate by Servicer Satellite Starting Location')
    plt.xlabel('Initial Mean Anomaly of Servicer Satellite (degrees)')
    plt.ylabel('Minimum Average Response Time (days)')
    plt.grid(True)
    return plt

def plotVaryingPriorityandBestPriAngleOrbital(xs, priTimes):
    plt.figure(figsize=(10, 6))
    plt.plot(xs, priTimes, label='Priority Queue')
    plt.title('Change in Optimal Priority Area Half Angle by Servicer Satellite Starting Location')
    plt.xlabel('Initial Mean Anomaly of Servicer Satellite (degrees)')
    plt.ylabel('Half Angle of Minimum Response Time (degrees)')
    plt.grid(True)
    return plt

def computeVaryingPrioritySquare(sideLength, buffer):
    region = StandardResponseArea(sideLength, 0)
    standardTime = region.computeResponseTime()

    # get priority queue times 
    xs = np.linspace(buffer, sideLength - buffer, 50)
    priTimes = []
    for i in range(len(xs)):
        region = PriorityResponseArea(sideLength, xs[i])
        priTimes.append(region.computeResponseTime())

    min_index = priTimes.index(min(priTimes))
    print('min time = ' + str(min(priTimes)) + " at side length = " + str(xs[min_index]))
    print(str(xs[min_index]/sideLength) + ' of the way')

    return [xs, priTimes, standardTime]

def plotVaryingPrioritySquare(xs, priTimes, standardTime, sideLength):
    plt.figure(figsize=(10, 6))
    plt.plot(xs, priTimes, label='Priority Queue')
    plt.plot([0, sideLength], [standardTime] * 2, label='Standard Queue')
    plt.title('Average Response Times for Queueing Types')
    plt.xlabel('Priority Area Side Length')
    plt.ylabel('Average Response Time (minutes)')
    plt.legend()
    plt.grid(True)
    return plt