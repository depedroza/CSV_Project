import csv
from shutil import which

sitka_file = open("sitka_weather_07-2018_simple.csv", "r")
sitka_infile = csv.reader(sitka_file, delimiter=",")

header_row = next(sitka_infile)

# print(type(header_row))

# hint for assignment
for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
for line in sitka_infile:
    # print(line[5])
    # above extracs item in index 5 of that line
    highs.append(int(line[5]))
print(highs)

import matplotlib.pyplot as plt

plt.plot(highs, c="red")

plt.title("Daily high temperatures, July 2018", fontsize=16)
plt.xlabel("")
plt.ylabel("Temperatures (F)")
plt.tick_params(axis="both", which="major", labelsize=16)

plt.show()
