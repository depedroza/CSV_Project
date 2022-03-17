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

highs = []
lows = []
dates = []

# test_date = datetime.strptime("2018-07-01", "%Y-%m-%d")
# print(test_date)

for line in sitka_infile:
    # print(line[5])
    # above extracs item in index 5 of that line
    highs.append(int(line[header_row.index("TMAX")]))
    lows.append(int(line[header_row.index("TMIN")]))
    date = datetime.strptime(line[header_row.index("DATE")], "%Y-%m-%d")
    dates.append(date)

valley_file = open("death_valley_2018_simple.csv", "r")
valley_infile = csv.reader(valley_file, delimiter=",")

header_row2 = next(valley_infile)

for index, column_header2 in enumerate(header_row2):
    print(index, column_header2)

highs2 = []
lows2 = []
dates2 = []

for line in valley_infile:

    try:
        current_date = datetime.strptime(line[header_row2.index("DATE")], "%Y-%m-%d")
        high = int(line[header_row2.index("TMAX")])
        low = int(line[header_row2.index("TMIN")])

    except ValueError:
        print(f"missing data for {current_date}")

    else:
        highs2.append(high)
        lows2.append(low)
        dates2.append(current_date)


fig = plt.figure()

plt.tick_params(axis="both", which="major", labelsize=16)
# plt.show()

plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
plt.title("SITKA AIRPORT, AK US", fontsize=16)
plt.ylabel("Temperatures (F)")


plt.subplot(2, 1, 2)
plt.plot(dates2, highs2, c="red")
plt.plot(dates2, lows2, c="blue")
plt.fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)
plt.title("DEATH VALLEY, CA US", fontsize=16)
plt.xlabel("YEAR - 2018")
plt.ylabel("Temperatures (F)")


plt.suptitle(
    "Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US"
)

fig.autofmt_xdate()

plt.show()
