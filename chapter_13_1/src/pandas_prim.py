import csv
import json
import pandas as pd


# data = {"student_id": ["001", "002", "003"], "name": ["German", "Alice", "Stue"], "grade": [87, 93, 69]}
#
# df = pd.DataFrame(data)
# df.set_index("student_id", inplace=True)

# with open("../data/winemag-data-130k-v2.csv", encoding="UTF-8") as f:
#     reader = csv.DictReader(f)
#     result = []
#     count = 0
#     for row in reader:
#         result.append(row)
#         count += 1
#         if count == 5:
#             break
#
# with open("prim.json", "w", encoding="UTF-8") as json_file:
#     json.dump(result, json_file, indent=4)
df = pd.read_excel("../data/winemag-data-130k-v2.xlsx")
print(df.loc[df.country.isin(["Italy", "France"])])
