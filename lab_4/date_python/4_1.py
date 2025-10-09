import datetime

x=datetime.datetime.now()

y=datetime.datetime.now()-datetime.timedelta(1)

x=datetime.datetime.timestamp(x)
y=datetime.datetime.timestamp(y)

print(x-y)