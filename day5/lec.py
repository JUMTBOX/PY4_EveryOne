import csv
import matplotlib.pyplot as plt

f = open("temp.csv", "r", encoding="cp949")
data = csv.reader(f)

header = next(data)
month = []
for i in range(12):
    month.append([])
for row in data:
    if row[4] != "":
        m = int(row[2].split("-")[1]) - 1
        month[m].append(float(row[4]))
plt.boxplot(month)
