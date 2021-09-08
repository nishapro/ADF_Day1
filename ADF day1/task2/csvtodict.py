import csv

filename = "csvfile.csv"
l=[]
with open(filename, 'r') as data:
    for line in csv.DictReader(data):
        l.append(line)
    print(l)
