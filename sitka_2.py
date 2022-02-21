# using the datetime module
# adding dates to the x axis for the month of July 2018

import csv
from datetime import datetime

sitka_file = open("sitka_weather_07-2018_simple.csv", "r")
sitka_infile = csv.reader(sitka_file, delimiter=",")

header_row = next(sitka_infile)

# print(type(header_row))

# hint for assignment
for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
dates = []

# test_date = datetime.strptime("2018-07-01", "%Y-%m-%d")
# print(test_date)

for line in sitka_infile:
    # print(line[5])
    # above extracs item in index 5 of that line
    highs.append(int(line[5]))
    date = datetime.strptime(line[2], "%Y-%m-%d")
    dates.append(date)
print(highs)
print(dates)

import matplotlib.pyplot as plt

fig = plt.figure()


plt.plot(dates, highs, c="red")


plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("Month of July 2018")
plt.ylabel("Temperatures (F)")
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.show()
