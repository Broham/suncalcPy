import unittest
import suncalc
from datetime import datetime
import pytz
# import math



class SunCalcTestCases(unittest.TestCase):
    """Tests for `suncalc.py`."""
    def near(self, val1, val2):
        # print "val1",val1
        # print "val2",val2
        return abs(val1 - val2) < (1E-15)
        # return abs(val1 - val2) < (margin or 1E-15)

    # local = pytz.timezone ("America/Los_Angeles")
    # naive = datetime.strptime ('2013-03-04 16','%Y-%m-%d %H')
    # local_dt = local.localize(naive, is_dst=None)
    # utc_dt = local_dt.astimezone (pytz.utc)
    # date = utc_dt
    date = datetime.strptime('2013-03-04 16','%Y-%m-%d %H')
    # date = date('2013-03-05UTC')
    lat = 50.5
    lng = 30.5


    # sunTimes = dict(
    #     # solarNoon = '2013-03-05 10:10:57Z',
    #     # wtf is nadir?  commenting out for now...
    #     # nadir = '2013-03-04T22:10:57Z',
    #     sunrise =       '2013-03-04 20:38:19',
    #     sunset =        '2013-03-04 21:19:01',
    #     sunriseEnd =    '2013-03-05 08:19:36',
    #     sunsetStart =   '2013-03-04 18:46:17',
    #     dawn =          '2013-03-05 09:35:36',
    #     dusk =          '2013-03-05 07:02:52',
    #     nauticalDawn =  '2013-03-05 07:46:57',
    #     nauticalDusk =  '2013-03-05 07:43:34',
    #     nightEnd =      '2013-03-04 19:24:31',
    #     night =         '2013-03-04 20:02:17',
    #     goldenHourEnd = '2013-03-05 08:57:22',
    #     goldenHour =    '2013-03-04 20:34:56')

    sunTimes = dict(
        # solarNoon = '2013-03-05 10:10:57Z',
        # wtf is nadir?  commenting out for now...
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
        date = datetime.strptime('2013-03-04 16','%Y-%m-%d %H')
        """Get sun positions correctly"""
        sunPos = suncalc.getPosition(date, self.lat, self.lng)
        print "sunpos", sunPos, "date", self.date
        self.assertTrue(self.near(sunPos["azimuth"], -2.5003175907168385) )
        self.assertTrue( self.near(sunPos["altitude"], -0.7000406838781611) )

    def test_getTimes(self):
        """Get sun times correctly"""
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
        moonPos = suncalc.getMoonPosition(date, self.lat, self.lng)
        self.assertTrue(self.near(moonPos["azimuth"], -0.9783999522438226))
        self.assertTrue(self.near(moonPos["altitude"], 0.006969727754891917))
        self.assertTrue(self.near(moonPos["distance"], 364121.37256256194))

if __name__ == '__main__':
    unittest.main()


# t.test('getTimes returns sun phases for the given date and location', function (t) {
#     var times = SunCalc.getTimes(date, lat, lng);

#     for (var i in testTimes) {
#         t.equal(new Date(testTimes[i]).toUTCString(), times[i].toUTCString(), i);
#     }
#     t.end();
# });

# t.test('getMoonPosition returns moon position data given time and location', function (t) {
#     var moonPos = SunCalc.getMoonPosition(date, lat, lng);

#     t.ok(near(moonPos.azimuth, -0.9783999522438226), 'azimuth');
#     t.ok(near(moonPos.altitude, 0.006969727754891917), 'altitude');
#     t.ok(near(moonPos.distance, 364121.37256256194), 'distance');
#     t.end();
# });

# t.test('getMoonIllumination returns fraction and angle of moon\'s illuminated limb and phase', function (t) {
#     var moonIllum = SunCalc.getMoonIllumination(date);

#     t.ok(near(moonIllum.fraction, 0.4848068202456373), 'fraction');
#     t.ok(near(moonIllum.phase, 0.7548368838538762), 'phase');
#     t.ok(near(moonIllum.angle, 1.6732942678578346), 'angle');
#     t.end();
# });

# t.test('getMoonTimes returns moon rise and set times', function (t) {
#     var moonTimes = SunCalc.getMoonTimes(date, lat, lng);

#     t.equal(moonTimes.rise.toUTCString(), 'Mon, 04 Mar 2013 23:57:55 GMT');
#     t.equal(moonTimes.set.toUTCString(), 'Tue, 05 Mar 2013 08:41:31 GMT');
#     t.end();
# });
