import csv

#write to csv
with open('some.csv', 'w') as wri:
    writer = csv.writer(wri, lineterminator='\n')
    writer.writerow(['ID', 'name'])
    writer.writerow(['001', 'Tanaka'])
    writer.writerow(['002', 'Yamada'])

#read from csv
with open('some.csv', 'r') as red:
    csv_reader = csv.reader(red, delimiter=',', quotechar='"')
    for row in csv_reader:
        print(','.join(row))