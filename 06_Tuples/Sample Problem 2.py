from datetime import datetime

n = int(input())

list_of_entries = []

for i in range(n):
    s = input()
    s = s.split(",")
    list_of_entries.append((s[0],s[1]))

filter_date = input()

filter_date_object = datetime.strptime(filter_date, '%d-%m-%Y').date()

print(list_of_entries)

for a,b in list_of_entries:
    item_date = datetime.strptime(b, '%d-%m-%Y').date()
    if(item_date >= filter_date_object):
        print(a)
