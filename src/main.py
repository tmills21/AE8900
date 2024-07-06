from parseTLE import *

# read in all satellites and propogate them in time to most recent one
filename = "./data/geoSmall.txt"
sats = TLEdata(filename)
[(newestYear, newestDay), (oldestYear, oldestYear)] = sats.getOldestAndNewest()
sats.propogateToSameTime(newestYear, newestDay)

# determine length of time to care about and failures (time and satellite)

# run model to service each failure, recording time it takes to service

# compute mean and variance