import csv

csv_file = open('trees.csv')
csv_reader = csv.reader(csv_file, delimiter=',')

# Skip first row if it only contains the column headers
next(csv_reader)
max_height = 0
max_vol = 0

for row in csv_reader:
    Index, Girth, Height, Volume = row
    if int(Height) > max_height:
        max_height = int(Height)
    if float(Volume) > max_vol:
        max_vol = float(Volume)

print("Heighest tree was {} meters high.".format(max_height))
print("Largest volume of the tree was {} m2".format(max_vol))

csv_file.close()

