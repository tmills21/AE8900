import math

class performService:
    def __init__(self, inc, ecc, n):

        # https://pdf.sciencedirectassets.com/779986/3-s2.0-C20200018736/3-s2.0-B9780128240250000064/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLWVhc3QtMSJIMEYCIQCFMZsm5bSaN1%2BoyEKKUaTDCeeu5xzL1V%2Fhem0pBVhkjAIhAIoYTFoyk3yVJqx9RwTLfE%2BbPG3PxxdBqFeSMWWy8E88KrIFCBsQBRoMMDU5MDAzNTQ2ODY1IgxRntdUr1j8A22aCWIqjwW%2FAfXqkDMoLfFNexxNRFrHBZHgobdvXieJ6V%2Bvp1KeW%2FDftSZfU1n3M7MN0oi96DYODrdt9jUVx%2BRU8Vbh2QdUcoDniRf2zRRalrWOIhqpIWL4wy8Fqxk%2BLrrZXNlG1Bt0SeYzPUra%2B4EBQsEbO2X8Sw193tXTU8VL%2BiFttwd1oQI8EtxViZmj26%2BHqMW7RhtxHdn%2Fiv9lSgSzfuVg2VyyhOR0D8loa0kaB3xavvhP62TaPrua5%2Bm%2BSued5M2ftkG62rTH1hCgGGhnhKtmknJ3mHW%2BImUlmbM8ebf25ZqD85l0ZcAaMu8mije7dkct3WTPQeh06wBnwGkApOICqHddlqBlRHJA4GCAIPy6AdS92T%2BHxF72lhfl9Uuc%2BA89YHiuLjh4DpRDMI%2FDS05N8vM2yAcs3JfnLC1WO2Eqzjd1paCb%2F9GSPIbPz4ea8D9j8saNBmUi%2BEZZc3fmtBYvNsd3wtKLioBuMRVBGkVfg7JqGp20ZKvuJI2opEshGaVhVCKw9s7hJdfT1UNEKGB5PZYJjGAaxWEcsEdnbAQOVN0pc3vLVN3qrS7GLRppfS4Y3EzkUbixbiKguwPBrOEoIICgis1vjeqHFRw7c8xWHiM2X4qZQUmW3mQt%2Bo6plhNskcN%2BXe%2FRcoAr9FDt%2BokVpd%2Fd6%2BmCdd8%2BY8FJRkQY0kvxZ5sB9VZusQ1AoCDDRzDCN2NfByVicjUjWCQYUp1lKdVwTwfj6jUXIAauPiTvG4MNZs2g08Ee22b%2BdB05sN%2BcI3XcrYEeJd%2FUmDVBkTu6kQnE8AVqo3IG79aOm%2Bxd3dj9qscQejvqQ9Z8UR4vFoEKtpJPpmGcPfhwYBjkUR5%2BSE10uIg%2FT%2FnDcmZljnsnPtsuMPmSmrUGOrABOeQN2jlb22u8l7hgMDRilzzJ1%2FLMR6T%2Bd2%2FVcC3XBcuocdOyt%2FKQDs9X%2BQIM%2BP1eMYLy2I5P6PMJKDconMnGgmk4WOv71N4WoEhdX3jk4f7xbBh5Dgie%2B1CKvD3Yx%2FlAshoBoh9xRJKVF0X570swm5MgWi1cdHpO%2BVYBR28wlwlHtwmqw5nzfUkWN9o18pld4Dy4KmaQOQzIs0rKvgtbXKaoX7jnej%2FGevV%2F3D2EV3k%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240728T190103Z&X-Amz-SignedHeaders=host&X-Amz-Expires=299&X-Amz-Credential=ASIAQ3PHCVTY2L6AYPEC%2F20240728%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=ad41dcd91dc1ef77c77093a6e71d8726a0dcee14d58c946c33652c44225b86ef&hash=983a149c9aa49ace205ac6d984155076fc82bdb49741c5207bbfcd4563f8defc&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=B9780128240250000064&tid=spdf-49566913-2eb2-4d76-a9d6-ebd860451f28&sid=3f59677392c0384ca73aa74182340d935d5agxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=131c5e06015257055952&rr=8aa71d978a973898&cc=us
        
        # booleans indicating if that orbital element should be simplified
        self.inc = inc
        self.ecc = ecc
        self.n = n

        # parameters for what is acceptable for the phasing orbit
        self.maxDeltaV = 200 # m/s
        self.minAlt = 150000 # m

        # constant for earth
        self.mu = 3.986004418 * 10**14 # m^3/s^2
        self.Re = 6378137 # m
        self.omegaE = 72.922 * 10**-6 # rad/s
        self.a = self.getafromn(1)
        self.vGEO = math.sqrt( self.mu / self.a )

    def simplifyOrbit(self, sat):
        if self.inc:
            sat['inclination'] = 0
            sat['Omega'] = 0

        if self.ecc:
            sat['eccentricity'] = 0
            sat['omega'] = 0

        if self.n:
            sat['n'] = 1

        a = self.getafromn(sat['n'])
        sat['a'] = a # Semi-major axis, meters
        sat['ra'] = a * ( 1 + sat['eccentricity'] )
        sat['rp'] = a * ( 1 - sat['eccentricity'] )

        return sat
    
    def getafromn(self, n):

        # https://space.stackexchange.com/questions/18289/how-to-get-semi-major-axis-from-tle
        num = self.mu**(1/3)
        denom = ( 2 * n * math.pi ) / 86400
        val = num / ( denom**(2/3) )
        return val # meters

    def getPhaseAngle(self, servicer, target):
        diff = servicer['M'] - target['M']

        if diff > math.pi:
            diff = ( 2 * math.pi ) - diff
        elif diff < - math.pi:
            diff = ( 2 * math.pi ) + diff

        # negative means chase, positive means slow down
        # print(math.degrees(diff))
        return diff

    def computeRevs(self, theta, n):

        # phasing orbit period
        T2 = ( 1 / n ) * ( theta + n * ( 2 * math.pi ) ) / self.omegaE # s

        if T2 < 0:
            # if phasing orbit is not achievable, return very large/nonsense values
            return [10e5, 0]

        # drift rate, not used, just interesting
        thetadot = theta / ( n * T2 ) # rad/s

        # phasing orbit semi-major axis
        a2 = ( ( T2 * math.sqrt(self.mu) ) / ( 2 * math.pi ) )**(2/3) # m

        # apogee or perigee of the phasing orbit
        if theta > 0:
            rp = self.a
            ra = 2 * a2 - self.a
            rc = ra
        else:
            rp = 2 * a2 - self.a
            ra = self.a
            rc = rp

        # if phasing orbit gets too close to earth, return very large/nonsense values
        if rp < ( self.Re + self.minAlt ):
            return [10e5, 0]

        # compute dv of maneuver
        h2 = math.sqrt( 2 * self.mu ) * math.sqrt( ( self.a * rc) / ( self.a + rc ) ) # m^2/s
        vp2 = h2 / self.a # m/s
        dv = 2 * abs( vp2 - self.vGEO ) # m/s

        # change in velocity and phasing orbit period
        return [dv, T2]
    
    def computeTimeHohmann(self, theta):

        # initialie variables
        counter = 0
        dv = 10e5
        m = 1
        n = 1

        # while the delta v is too large
        while dv > self.maxDeltaV:

            # round trip dv
            dv1, T21 = self.computeRevs(theta, m)
            dv2, T22 = self.computeRevs(-theta, n)
            dv = dv1 + dv2

            # add more revolutions to the orbits, starting with the more difficult maneuver
            if theta < 0:
                if counter % 2 == 0:
                    m += 1
                else:
                    n += 1
            else:
                if counter % 2 == 1:
                    m += 1
                else:
                    n += 1

            counter += 1

        # return total trip time
        time = T21 * m + T22 * n # s
        return time