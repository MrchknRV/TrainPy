import csv

with open("../data/students.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")
    # next(reader)
    for row in reader:
        name, age, avg_grade = row
        if float(avg_grade) > 4.5:
            print(f"{name} ({age} age) - average goal: {avg_grade}")
