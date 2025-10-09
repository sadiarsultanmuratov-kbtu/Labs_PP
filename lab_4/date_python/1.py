import datetime

x=datetime.datetime.now()

y=x-datetime.timedelta(days=5)

print(y.strftime("%Y-%M-%d"))
