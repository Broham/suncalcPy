import unittest
import suncalc
from datetime import datetime
import pytz



class SunCalcTestCases(unittest.TestCase):
    """Tests for `suncalc.py`."""
    def near(self, val1, val2):
        return abs(val1 - val2) < (1E-15)

    date = datetime.strptime('2013-03-04 16','%Y-%m-%d %H')
    lat = 50.5
    lng = 30.5


    sunTimes = dict(
        # solarNoon = '2013-03-05 10:10:57Z',
        # nadir = '2013-03-04T22:10:57Z',
        sunrise = '2013-03-05 04:34:56',
        sunset = '2013-03-05 15:46:57',
        sunriseEnd = '2013-03-05 04:38:19',
        sunsetStart = '2013-03-05 15:43:34',
        dawn = '2013-03-05 04:02:17',
        dusk = '2013-03-05 16:19:36',
        nauticalDawn = '2013-03-05 03:24:31',
        nauticalDusk = '2013-03-05 16:57:22',
        nightEnd = '2013-03-05 02:46:17',
        night = '2013-03-05 17:35:36',
        goldenHourEnd = '2013-03-05 05:19:01',
        goldenHour = '2013-03-05 15:02:52')


    def test_getPositions(self):
        """Get sun positions correctly"""
        sunPos = suncalc.getPosition(self.date, self.lat, self.lng)
        self.assertTrue(self.near(sunPos["azimuth"], -2.5003175907168385) )
        self.assertTrue( self.near(sunPos["altitude"], -0.7000406838781611) )

    def test_getTimes(self):
        """Get sun times correctly"""
        # Weirdness to handle PST to UTC date/time comparisons.  Consider moving everything to PST instead of having this conversion?
        local = pytz.timezone ("America/Los_Angeles")
        naive = datetime.strptime ('2013-03-04 16','%Y-%m-%d %H')
        local_dt = local.localize(naive, is_dst=None)
        utc_dt = local_dt.astimezone (pytz.utc)
        times = suncalc.getTimes(utc_dt, self.lat, self.lng)

        for i in self.sunTimes:
            naive = datetime.strptime (times[i],'%Y-%m-%d %H:%M:%S')
            local_dt = local.localize(naive, is_dst=None)
            utc_dt = local_dt.astimezone (pytz.utc)
            self.assertEqual(self.sunTimes[i],utc_dt.strftime('%Y-%m-%d %H:%M:%S'))

    def test_getMoonPosition(self):
        """Get Moon position correctly"""
        date = datetime.strptime('2013-03-04 16','%Y-%m-%d %H')
        moonPos = suncalc.getMoonPosition(self.date, self.lat, self.lng)
        self.assertTrue(self.near(moonPos["azimuth"], -0.9783999522438226))
        self.assertTrue(self.near(moonPos["altitude"], 0.006969727754891917))
        self.assertTrue(self.near(moonPos["distance"], 364121.37256256194))

    def test_getMoonIllumination(self):
        """Get moon illumination correctly"""
        moonIllum = suncalc.getMoonIllumination(self.date)
        self.assertTrue(self.near(moonIllum["fraction"], 0.4848068202456373))
        self.assertTrue(self.near(moonIllum["phase"], 0.7548368838538762))
        self.assertTrue(self.near(moonIllum["angle"], 1.6732942678578346))

    def test_getMoonTimes(self):
        moonTimes = suncalc.getMoonTimes(self.date, self.lat, self.lng)
        self.assertEqual(moonTimes["rise"].strftime('%Y-%m-%d %H:%M:%S'), '2013-03-04 15:57:55')
        # self.assertEqual(moonTimes["rise"].strftime('%Y-%m-%d %H:%M:%S'), '2013-03-04 23:57:55')

if __name__ == '__main__':
    unittest.main()

