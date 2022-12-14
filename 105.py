import pytz
from persiantools.jdatetime import JalaliDateTime

print(JalaliDateTime(1401, 9, 23, 19, 42, 10, 0, pytz.utc).strftime("%A"))
