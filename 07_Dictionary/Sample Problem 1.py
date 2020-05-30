from datetime import datetime
from datetime import timedelta

date1 = input()
date2 = input()

n = int(input())

date1_format = datetime.strptime(date1, '%b %d %Y')
date2_format = datetime.strptime(date2, '%b %d %Y')

days_available = date1_format - date2_format
days_to_expiry = timedelta(days=n)

if(days_to_expiry < days_available):
    print("Yes")
else:
    print("No")