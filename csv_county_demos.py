"""
program :csv_county_demos.py
author: kyle godwin
last date modified: 05 april 2023
"""
import csv
from county_demos_class import CountyDemos as CD

with open('ExampleCSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    county = {}

    for row in csv_reader:
        # The first row is treated differently because it is the header row
        if line_count == 0:
            line_count += 1
            continue
        county[str(row[0])] = CD(row[1], row[2])
    print(f"processed {line_count} rows")

if __name__ == "__main__":
    print(county)
    print(county['Polk'].population)
    print(county["Dickinson"].num_households)
