import csv

f = open("../대전기상데이터.csv", "r")

data = csv.reader(f)
# header = next(data)

for row in data:
    if row[4] == "":
        row[4] = 999
    else:
        row[4] = float(row[4])
    print(row[4])
f.close()
