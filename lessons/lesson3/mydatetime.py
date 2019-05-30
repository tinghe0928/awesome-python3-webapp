#! /usr/bin/env python3

from datetime import datetime
from datetime import timedelta
from datetime import timezone

#
# datetime()
# datetime.now()
#
# datetime.timestamp()
# datetime.fromtimestamp()
#
# datetime.date()
# datetime.time()
#
# datetime.strptime()
#
# datetime.strftime()
# timedelta(years=1,seconds=10)
print(datetime.now().replace(tzinfo=timezone(timedelta(hours=8))))

dt = datetime.now()
# print(dt)
#
# dtstamp = datetime.timestamp(dt)
# print(dtstamp)
#
# print(datetime.date(dt))
# print(datetime.time(dt))
# dt = datetime(1990,9,28,19,0,0)
# print(dt)
# print(datetime.timestamp(dt))

# dt = datetime.strptime(str(dt)[:19],'%Y-%m-%d %H:%M:%S')
#
# # print(dt.strftime('%a, %b %d %H:%M:%S'))
# print(dt.strftime('%Y-%m-%d %H:%M:%S'))
# print(dt)

dt1 = dt + timedelta(days=2,hours=10)
print(dt1)
