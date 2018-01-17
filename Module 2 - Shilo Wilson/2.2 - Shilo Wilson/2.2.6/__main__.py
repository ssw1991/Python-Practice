"""
Jan 14, 2018
Author: Shilo Wilson

Main function to test the loan class.

"""

from assets.Car.Civic import Civic as Civic
from assets.Car.Lexus import Lexus as Lexus
from assets.House.PrimaryHome import PrimaryHome as Primary
from assets.House.VacationHome import VacationHome as Vacation
def main():
    print ('========== Exercise 2.2.6 ==========\n')

    assets = [
        Civic(12000),
        Lexus(45000),
        Primary(250000),
        Vacation(100000)
    ]

    for i in assets:
        print 'Monthly Depreciation {}, value after 1 year {}'. format(i.monthlyDepreciation(), i.currentvalue(12))



if __name__ == '__main__':
    main()