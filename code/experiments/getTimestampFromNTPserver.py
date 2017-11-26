import ntplib
import time
import datetime
from time import ctime


c = ntplib.NTPClient()
print("before call",datetime.datetime.now())
response = c.request('pool.ntp.org')
seconds_microseconds = str(response.tx_timestamp).split(".")
print(response.tx_time)
print("after call",datetime.datetime.now())
microseconds = int(seconds_microseconds[1])

print(datetime.datetime.now())
print(response.tx_timestamp - int(response.tx_timestamp))
time.sleep(1)
response = c.request('pool.ntp.org')
print(response.tx_timestamp)
print("call for time",datetime.datetime.now())
print("call for time",datetime.datetime.now())
print("call for time",datetime.datetime.now())
print("call for time",datetime.datetime.now())
print("call for time",datetime.datetime.now())
print("call for time",datetime.datetime.now())

c = ntplib.NTPClient()
print(datetime.datetime.now())
response = c.request('pool.ntp.org')
print(response.tx_time)
datetime.datetime.now()