import csv

res = {}
with open('queryResults-bo.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        res[row[0]] = row
with open('queryResults-bozh.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        res[row[0]] = row
with open('merged.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    for _, row in res.items():
        spamwriter.writerow(row)