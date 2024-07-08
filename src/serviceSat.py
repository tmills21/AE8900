class ServiceSatellite:
    def __init__(self, year, day):

        # defines a circular geostationary orbit
        self.serviceSat = dict()
        self.serviceSat['name'] = 'serve'

        self.serviceSat['epochYear'] = year
        self.serviceSat['epochDay'] = day

        self.serviceSat['inclination'] = 0
        self.serviceSat['Omega'] = 0 # should not matter for circular geostationary
        self.serviceSat['eccentricity'] = 0 # circle
        self.serviceSat['omega'] = 0 # technically not defined, defaulted to 0
        self.serviceSat['M'] = 0 # Mean Anomaly, radians
        self.serviceSat['n'] = 1 # Mean Motion, revs/day
