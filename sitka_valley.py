import csv
from datetime import datetime
import matplotlib.pyplot as plt
from numpy import arange

sitka_file = open("sitka_weather_2018_simple.csv", "r")
sitka_infile = csv.reader(sitka_file, delimiter=",")

header_row = next(sitka_infile)

# hint for assignment
for index, column_header in enumerate(header_row):
    print(index, column_header)

high1 = []
low1 = []
date1 = []
area1 = []

highs = header_row.index("TMAX")
lows = header_row.index("TMIN")
dates = header_row.index("DATE")
name_index = header_row.index("NAME")


for line in sitka_infile:
    high1.append(int(line[highs]))
    low1.append(int(line[lows]))
    date_get = datetime.strptime(line[dates], "%Y-%m-%d")
    date1.append(date_get)


fig = plt.figure()


plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.title("Daily low and high temperatures - 2018", fontsize=16)
plt.xlabel("YEAR - 2018")
plt.ylabel("Temperatures (F)")
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

valley_file = open("death_valley_2018_simple.csv", "r")
valley_infile = csv.reader(valley_file, delimiter=",")

header_row2 = next(valley_infile)

for index, column_header2 in enumerate(header_row2):
    print(index, column_header2)

high2 = []
low2 = []
date2 = []
area2 = []

highs = header_row2.index("TMAX")
lows = header_row2.index("TMIN")
dates = header_row2.index("DATE")
name_index = header_row2.index("NAME")

for line in valley_infile:
    high2.append(int(line[highs]))
    low2.append(int(line[lows]))
    date_get = datetime.strptime(line[dates], "%Y-%m-%d")
    date2.append(date_get)

plt.plot(date2, high2, c="red")
plt.plot(date2, low2, c="blue")

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.title("Daily low and high temperatures - 2018", fontsize=16)
plt.xlabel("YEAR - 2018")
plt.ylabel("Temperatures (F)")
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.title("Highs")

plt.subplot(2, 1, 2)
plt.plot(dates, lows, c="blue")
plt.title("Lows")

plt.suptitle("Temperature Comparison - Sitka Airport and Death Valley")

plt.show()
