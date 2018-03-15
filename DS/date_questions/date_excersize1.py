import datetime
import pytz
import time
import calendar


today = datetime.date.today()

print(today)

daysfrom_today = datetime.timedelta(days=7)

print(today-daysfrom_today)
print(today+daysfrom_today)

# Calculate number of days till birthday
# date2 = date1 + timedelta
# timedelta = date1 +- date2

bday = datetime.date(2017,5,25)

till_day = bday-today

print(till_day)
print(till_day.days)
print(till_day.total_seconds())
print(bday.month)

print("weekday",today.weekday())      #[Monday 0, Sunday 6]
print(today.isoweekday())             #[Monday 1, Sunday 7]
print(today.isocalendar())

time_var = datetime.time(9,30,45,100000)
print(time_var)
print(time_var.hour)

dt_time = datetime.datetime(2016,7,26,12,30,45,10000)
print(dt_time)
print(dt_time.date())
print(dt_time.time())
print(dt_time.year)

tdelta = datetime.timedelta(days=7)
print(dt_time+tdelta)

print("=============================================")
tdelta_min = datetime.timedelta(minutes=7)
print("time delta in minutes ", tdelta_min)


tdelta_sec = datetime.timedelta(seconds=7)
print("time delta in minutes ", tdelta_sec)


tdelta_hour = datetime.timedelta(hours=7)
print("time delta in minutes ", tdelta_hour)

print("=============================================")


dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()   #Timezone, if nothing passed no timezine, similar to today()
dt_utc = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utc)
print(datetime.datetime.utcnow())

# for tz in pytz.all_timezones:
#     print(tz)

print("=============================================")

dt_str = "July 26, 2017"

dt = datetime.datetime.strptime(dt_str,'%B %d, %Y')
print(dt)

#strftime :- datetime to string
#strptime :- string to datetime



print(time.localtime(time.time()))
print(time.asctime())

print("=============================================")


#print(calendar.month(2017,5))
print(calendar.isleap(2017))
print("=============================================")

s = "this is a string"
print(" ".join(s.split()[::-1]))

print(' '.join([x[::-1] for x in s.split(' ')]))

print("=============================================")

for i in range(5,12):
    sent = "The value is    {:03}".format(i)
    print(sent)

print("=============================================")


pi = 3.14567
sent = 'pi is eqal to {:.2f}'.format(pi)
print(sent)

sent = "1 mb is equal to {:,.2f} bytes".format(1000**2)
print(sent)