import math

class utility:
    def __init__(self):
        # constants for earth
        self.mu = 3.986004418 * 10**14 # m^3/s^2
        self.Re = 6378137 # m
        self.omegaE = 72.922 * 10**-6 # rad/s

    def getafromn(self, n):

        # https://space.stackexchange.com/questions/18289/how-to-get-semi-major-axis-from-tle
        num = self.mu**(1/3)
        denom = ( 2 * n * math.pi ) / 86400
        val = num / ( denom**(2/3) )
        return val # meters