"""
program: census_data_csv.py
author: kyle godwin
last date modified: 05 april 2023
"""
import csv
from census_data_class import CensusData as CD

with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    county = {}

    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        county[str(row[1])] = CD(row[0], row[2], row[3], row[4], row[5], row[6])
    print(f"processed {line_count} rows")

    del county["United States"]
    del county["Iowa State"]


def pop_per_house(c):
    return int(county[c].population.replace(",", "")) / int(county[c].households.replace(",", ""))


def total_pop(county_lib):
    iowa_pop = 0
    for key in county_lib:
        #if not key == "United States" and key == "Iowa State":
            #iowa_pop = iowa_pop + int(county[key].population.replace(",", ""))
        iowa_pop = iowa_pop + int(county[key].population.replace(",", ""))
    return iowa_pop


if __name__ == "__main__":
    print(county)
    print(county["Dallas"].population)
    print(pop_per_house("Dallas"))
    print(total_pop(county))
