import datetime

x=datetime.datetime.now()

y=datetime.datetime.now()-datetime.timedelta(1)

z=x-y

print(z.seconds)