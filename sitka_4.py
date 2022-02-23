# 1) changin file to include all data for year 2018
# 2) change the title to - Daily low and high temperatures - 2018
# 3) extract low temps from the file and add to chart
# 4) shade in the area between hig hand low

import csv
from datetime import datetime

valley_file = open("death_valley_2018_simple.csv", "r")
valley_infile = csv.reader(valley_file, delimiter=",")

header_row = next(valley_infile)

# print(type(header_row))

# hint for assignment
for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
lows = []
dates = []

# test_date = datetime.strptime("2018-07-01", "%Y-%m-%d")
# print(test_date)

for line in valley_infile:

    try:
        current_date = datetime.strptime(line[2], "%Y-%m-%d")
        high = int(line[4])
        low = int(line[5])

    except ValueError:
        print(f"missing data for {current_date}")

    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

print(highs)
print(lows)
print(dates)


import matplotlib.pyplot as plt

fig = plt.figure()


plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")

plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

plt.title("Daily low and high temperatures - 2018", fontsize=16)
plt.xlabel("YEAR - 2018")
plt.ylabel("Temperatures (F)")
plt.tick_params(axis="both", which="major", labelsize=16)

fig.autofmt_xdate()

plt.show()
