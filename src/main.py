from parseTLE import *
from serviceSat import *

# read in all satellites and propogate them in time to most recent one
filename = "./data/geoSmall.txt"
sats = TLEdata(filename)
[(newestYear, newestDay), (oldestYear, oldestYear)] = sats.getOldestAndNewest()
sats.propogateToSameTime(newestYear, newestDay)
servicer = ServiceSatellite(newestYear, newestDay)

# determine length of time to care about and failures (time and satellite)
# TODO change to meaningful number, random for now
failureRateLambda = 0.5 # calls/year


# run model to service each failure, recording time it takes to service

# compute mean and variance