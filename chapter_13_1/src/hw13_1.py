import csv
import json
import pandas as pd


df = pd.read_excel("../data/transactions_excel.xlsx", dtype=str, engine="openpyxl")
transactions = df.to_dict(orient="records")

print(json.dumps(transactions))

# with open("../data/transactions.csv", encoding="cp1251") as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=";")
#     result = list(reader)
#
# with open("transaction.json", "w", encoding="cp1251") as f:
#     json.dump(result, f, indent=4)
