"""
program: census_data_class.py
author: kyle godwin
last date modified: 05 april 2023
"""


class CensusData:
    """CensusData class"""
    def __init__(self, rank, pc_income, house_income, fam_income, pop, houses):
        self.rank = rank
        # self.county = county
        self.percapita_income = pc_income
        self.household_income = house_income
        self.family_income = fam_income
        self.population = pop
        self.households = houses
