import math

class serviceSatellite:
    def __init__(self, year, day, M, n = 1):

        # defines a circular geostationary orbit at a specified mean anomaly
        self.serviceSat = dict()
        self.serviceSat['name'] = 'serve'

        self.serviceSat['epochYear'] = year
        self.serviceSat['epochDay'] = day

        self.serviceSat['inclination'] = 0
        self.serviceSat['Omega'] = 0 # should not matter for circular geostationary
        self.serviceSat['eccentricity'] = 0 # circle
        self.serviceSat['omega'] = 0 # technically not defined, defaulted to 0
        self.serviceSat['M'] = math.radians(M) % (2 * math.pi) # Mean Anomaly, radians
        self.serviceSat['n'] = n # Mean Motion, revs/day