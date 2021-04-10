from datetime import datetime
from pprint import pprint
from datetime import date

from adhan import adhan
from adhan.methods import ISNA, ASR_STANDARD

now = datetime.now()
now = now.strftime('%Y-%m-%d %H:%M:00')
print(now)


params = {}
params.update(ISNA)
params.update(ASR_STANDARD)

adhan_times = adhan(
    day=date.today(),
    location=(30.25,-97.75),
    parameters=params,
    timezone_offset=-6,
)

# pprint(adhan_times)
for i in adhan_times:
    print(adhan_times[i])

"""
adhan_times will be a dict containing datetime objects for the keys 'fajr',
'shuruq', 'zuhr', 'asr', 'maghrib', and 'isha'

""""""
"""
