import datetime
import random

f = open("temperature.csv", "w+")
f.write("Date,Temp\n")

for i in range(0, 60 * 24 * 365, 30):
    x = datetime.datetime.now() + datetime.timedelta(minutes=i)
    if datetime.timedelta(minutes=i).days % 5 == 0:
        f.write("{},{}\n".format(x.strftime("%Y-%m-%d %H:%M"), random.randint(0, 30)))
