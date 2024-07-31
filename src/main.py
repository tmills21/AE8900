from TLEdataClass import *
from serviceSatelliteClass import *
from performSimpleServiceClass import *
from responseTimeClass import *

import numpy as np
import matplotlib.pyplot as plt

# read in all satellites and propogate them in time to most recent one
filename = "./data/geo.txt"
sats = TLEdata(filename)
[(newestYear, newestDay), (oldestYear, oldestYear)] = sats.getOldestAndNewest()
sats.propogateToSameTime(newestYear, newestDay)
servicer = serviceSatellite(newestYear, newestDay)

# # get round trip time to all sats
# numSats = len(sats.satellites)
# serviceTimes = []
# service = performSimpleService(True, True, True)

# for i in range(numSats):

#     # simplify the orbit to circular GEO
#     target = service.simplifyOrbit(sats.satellites[i])

#     # get angle between servicer and target
#     theta = service.getPhaseAngle(servicer.serviceSat, target)

#     # compute time for there and back
#     time = service.computeTime(theta)
#     serviceTimes.append((theta, time))

# # compute mean and variance
# response = responseTime(serviceTimes)
# standardResponse = response.standardResponseTime()

# # get priority queue times 
# buffer = 0.5
# xs = np.linspace(buffer, 180 - buffer, 500)
# priTimes = []
# for i in range(len(xs)):
#     priTimes.append(response.priorityResponseTime(xs[i]))

# min_index = priTimes.index(min(priTimes))
# print('min time = ' + str(min(priTimes)) + " at side length = " + str(xs[min_index]))
# print(str(xs[min_index]/180) + ' of the way')

# plt.figure(figsize=(10, 6))
# plt.plot(xs, priTimes, label='Priority Queue')
# plt.plot([0, 180], [standardResponse] * 2, label='Standard Queue')
# plt.title('Average Response Times for Queueing Types')
# plt.xlabel('Half Angle of Priority (degrees)')
# plt.ylabel('Average Response Time (days)')
# plt.legend()
# plt.grid(True)
# plt.show()



# get round trip time to all sats
numSats = len(sats.satellites)
serviceTimes = []
service = performSimpleService(True, True, False)

for i in range(numSats):

    # simplify the orbit to circular GEO
    target = service.simplifyOrbit(sats.satellites[i])

    # get angle between servicer and target
    theta = service.getPhaseAngle(servicer.serviceSat, target)

    # compute time for there and back
    time = service.computeTime(theta)
    serviceTimes.append((theta, time))

# compute mean and variance
response = responseTime(serviceTimes)
standardResponse = response.standardResponseTime()

# get priority queue times 
buffer = 0.5
xs = np.linspace(buffer, 180 - buffer, 500)
priTimes = []
for i in range(len(xs)):
    priTimes.append(response.priorityResponseTime(xs[i]))

min_index = priTimes.index(min(priTimes))
print('min time = ' + str(min(priTimes)) + " at side length = " + str(xs[min_index]))
print(str(xs[min_index]/180) + ' of the way')

plt.figure(figsize=(10, 6))
plt.plot(xs, priTimes, label='Priority Queue')
plt.plot([0, 180], [standardResponse] * 2, label='Standard Queue')
plt.title('Average Response Times for Queueing Types')
plt.xlabel('Half Angle of Priority (degrees)')
plt.ylabel('Average Response Time (days)')
plt.legend()
plt.grid(True)
plt.show()