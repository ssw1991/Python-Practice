"""
Jan 14, 2018
Author: Shilo Wilson

Main function to test the loan class.

"""

from assets.Car.Civic import Civic as Civic
from assets.Car.Lexus import Lexus as Lexus
from assets.House.PrimaryHome import PrimaryHome as Primary
from assets.House.VacationHome import VacationHome as Vacation
from FixedRateMortgage import FixedRateMortgage as FixedMortgage
from FixedAutoLoan import FixedAutoLoan as Auto
def main():
    print ('========== Exercise 2.2.7 ==========\n')

    myHome = Primary(200000)
    myVacation = Vacation(300000)
    myCivic = Civic(20000)
    myLexus = Lexus(35000)

    loan1 = FixedMortgage(myHome, 360, .045, 195000)
    loan2 = FixedMortgage(myVacation, 180, .045, 250000)
    loan3 = Auto(myCivic, 48, .0675, 22000)
    loan4 = Auto(myLexus, 60, .055, 35000)

    print 'House Recovery Value in period 120: {}'.format(loan1.recoveryValue(120))
    print 'Vacation Home equity in period 240: {}'.format(loan2.equity(240))
    print 'Civic Equity when paid off {}'.format(loan3.equity(48))
    print 'Lexus recovery value after 1 year: {}'.format(loan4.recoveryValue(12))


if __name__ == '__main__':
    main()