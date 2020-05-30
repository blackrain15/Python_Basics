from datetime import datetime, timedelta

start_day = input()
days_to_reach = int(input())
start_date = input()

week_days = {'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}

start_date = datetime.strptime(start_date, '%d-%m-%Y')

start = week_days.get(start_day)
start = start+1
i=1
while(i<days_to_reach):
    
    if(start == 6):
        start = start+1
        start_date = start_date + timedelta(days=1)
    elif(start == 7):
        start = 1
        start_date = start_date + timedelta(days=1)
    else:
        i += 1
        start = start+1
        start_date = start_date + timedelta(days=1)
        print(start_date.strftime('%d-%m-%Y'))