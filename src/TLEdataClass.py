import math

class TLEdata:
    def __init__(self, filename):
        self.filename = filename
        self.satellites = self.parse()
        
    def parse(self):

        # Read TLE file
        with open(self.filename, "r") as f:
            tle_lines = f.readlines()

        all_satellites = dict()
        counter = 1
        for i in range(len(tle_lines)):
            if i%3 == 0:
                all_satellites[counter] = {'name' : tle_lines[i].strip()}
            
            if i%3 == 1:
                year = int(tle_lines[i][18:20]) + 1900
                if year < 1957:
                    year += 100
                all_satellites[counter]['epochYear'] = year # year
                all_satellites[counter]['epochDay'] = float(tle_lines[i][20:32]) # day of the year and fractional portion of the day

            if i%3 == 2:
                all_satellites[counter]['inclination'] = math.radians(float(tle_lines[i][8:16])) # radians
                all_satellites[counter]['Omega'] = math.radians(float(tle_lines[i][17:25])) # Right Ascension of Ascending Node (RAAN), radians
                all_satellites[counter]['eccentricity'] = float(tle_lines[i][26:33]) * 1e-7 
                all_satellites[counter]['omega'] = math.radians(float(tle_lines[i][34:42])) # Argument of Perigee, radians
                all_satellites[counter]['M'] = math.radians(float(tle_lines[i][43:51])) # Mean Anomaly, radians
                all_satellites[counter]['n'] = float(tle_lines[i][52:63]) # Mean Motion, revs/day
                counter += 1

        return all_satellites

    def getOldestAndNewest(self):
        oldestYear = None
        oldestDay = None
        newestYear = None
        newestDay = None

        for sat in self.satellites.values():
            candidateYear = sat['epochYear']
            candidateDay = sat['epochDay']

            if oldestYear is None or candidateYear <= oldestYear:
                if candidateYear == oldestYear:
                    if candidateDay <= oldestDay:
                        oldestYear = candidateYear
                        oldestDay = candidateDay
                else:
                    oldestYear = candidateYear
                    oldestDay = candidateDay

            if newestYear is None or candidateYear >= newestYear:
                if candidateYear == newestYear:
                    if candidateDay >= newestDay:
                        newestYear = candidateYear
                        newestDay = candidateDay
                else:
                    newestYear = candidateYear
                    newestDay = candidateDay

        return [(newestYear, newestDay), (oldestYear, oldestYear)]

    def propogateToSameTime(self, goalYear, goalDay):

        # TODO this assumes all the same year, which is true for geo.txt
        for sat in self.satellites.values():
            curYear = sat['epochYear']
            curDay = sat['epochDay']

            # get time needed to propogate
            daysToProp = goalDay - curDay
            secsToProp = daysToProp * 24 * 60 * 60

            # update the epoch and mean anomaly
            sat['epochYear'] = goalYear
            sat['epochDay'] = goalDay
            sat['M'] += sat['n'] * 2 * math.pi * daysToProp

if __name__ == "__main__":
    filename = "./data/geoSmall.txt"
    sats = TLEdata(filename)
    [(newestYear, newestDay), (oldestYear, oldestYear)] = sats.getOldestAndNewest()
    sats.propogateToSameTime(newestYear, newestDay)
    print(sats.satellites[1])