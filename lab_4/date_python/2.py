import datetime
x=datetime.date.today()-datetime.timedelta(1)
print("yesterday: "+str(x))

y=datetime.date.today()
print("today: "+str(y))

z=datetime.date.today()+datetime.timedelta(1)
print("today: "+str(z))
