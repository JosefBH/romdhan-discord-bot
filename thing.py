from pprint import pprint
from prayertimes.prayertimes import PrayTimes
import datetime

today = datetime.date.today()

# Using ISNA calculation method
PT = PrayTimes('ISNA')

# Date today
# City Lat and Long : 43, -80
# City UTC offset : -5 (you have to take into account DST)
times = PT.get_times(today, (43, -80), -5)
pprint(times)
