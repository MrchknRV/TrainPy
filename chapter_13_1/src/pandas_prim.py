import csv


with open("../data/winemag-data-130k-v2.csv") as f:
    wine_data = csv.DictReader(f)
    next(wine_data)
    count = 0
    for row in wine_data:
        print(row)
        count += 1
        if count == 5:
            break
