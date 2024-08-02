from serviceAreaSquareClass import *

import matplotlib.pyplot as plt
import numpy as np
import math

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
    plt.plot([0, 180], [standardTime] * 2, label='Standard Queue', color='#1f77b4')
    plt.plot(xs, priTimes, label='Priority Queue', color='#ff7f0e')
    plt.title('Average Service Times for Queueing Types')
    plt.xlabel('Half Angle of Priority (degrees)')
    plt.ylabel('Average Service Time (days)')
    plt.legend()
    plt.grid(True)
    return plt

def plotVaryingPriorityandAnomalyOrbital(xs, priTimes, standardTimes):
    plt.figure(figsize=(10, 6))
    plt.plot(xs, standardTimes, label='Standard Queue', color='#1f77b4')
    plt.plot(xs, priTimes, label='Priority Queue', color='#ff7f0e')
    plt.title('Change in Minimum Average Service Rate by Servicer Satellite Starting Location')
    plt.xlabel('Initial Mean Anomaly of Servicer Satellite (degrees)')
    plt.ylabel('Minimum Average Service Time (days)')
    plt.legend()
    plt.grid(True)
    return plt

def plotVaryingPriorityandBestPriAngleOrbital(xs, priTimes):
    plt.figure(figsize=(10, 6))
    plt.plot(xs, priTimes, label='Priority Queue')
    plt.title('Change in Optimal Priority Area Half Angle by Servicer Satellite Starting Location')
    plt.xlabel('Initial Mean Anomaly of Servicer Satellite (degrees)')
    plt.ylabel('Half Angle of Minimum Service Time (degrees)')
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
    plt.plot([0, sideLength], [standardTime] * 2, label='Standard Queue', color='#1f77b4')
    plt.plot(xs, priTimes, label='Priority Queue', color='#ff7f0e')
    plt.title('Average Service Times for Queueing Types')
    plt.xlabel('Priority Area Side Length')
    plt.ylabel('Average Service Time (minutes)')
    plt.legend()
    plt.grid(True)
    return plt

def plotSatelliteDistribution(sats):
    data = [math.degrees(sats[i]['M']) for i in range(len(sats))]

    # Create a histogram
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=10, edgecolor='black')

    # Add a title and labels
    plt.title('Epoch Target Satellite Mean Anomaly Histogram')
    plt.xlabel('Mean Anomaly (degrees)')
    plt.ylabel('Number of Satellites')

    return plt

def writeNewTLE(filename, sats, newestYear, newestDay, allSimp=False, newFilename="TLE_update.txt"):
    # Read TLE file
    with open(filename, "r") as readFile:
        tle_lines = readFile.readlines()

    with open(newFilename, "w") as writeFile:

        counter = 0
        for i in range(len(tle_lines)):
            if i%3 == 0:
                writeFile.write(tle_lines[i])
            
            if i%3 == 1:
                writeFile.write(tle_lines[i][0:18] + str(newestYear)[2:4] + str(newestDay) + tle_lines[i][32:])

            if i%3 == 2:
                if allSimp:
                    writeFile.write(tle_lines[i][:8] + '000.0000 000.0000 0000000 000.0000 ' + str(math.degrees(sats[counter]['M']))[:8] + '  1.00000000' + tle_lines[i][63:])
                else:
                    writeFile.write(tle_lines[i][:43] + str(math.degrees(sats[counter]['M']))[:8] + tle_lines[i][51:])

                counter += 1