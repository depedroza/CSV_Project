# 1) changin file to include all data for year 2018
# 2) change the title to - Daily low and high temperatures - 2018
# 3) extract low temps from the file and add to chart
# 4) shade in the area between hig hand low

import csv
from datetime import datetime

sitka_file = open("sitka_weather_2018_simple.csv", "r")
sitka_infile = csv.reader(sitka_file, delimiter=",")

header_row = next(sitka_infile)

# print(type(header_row))

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
    highs.append(int(line[5]))
    lows.append(int(line[6]))
    date = datetime.strptime(line[2], "%Y-%m-%d")
    dates.append(date)

print(highs)
print(lows)
print(dates)


import matplotlib.pyplot as plt

fig = plt.figure()

"""
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.title("Daily low and high temperatures - 2018", fontsize=16)
plt.xlabel("YEAR - 2018")
plt.ylabel("Temperatures (F)")
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.show()
"""
plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.title("Highs")

plt.subplot(2, 1, 2)
plt.plot(dates, lows, c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, AL 2018")

plt.show()
