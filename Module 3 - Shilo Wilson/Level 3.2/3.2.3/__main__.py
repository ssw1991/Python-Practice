"""
Jan 14, 2018
Author: Shilo Wilson

3) Modify your LoanPool class to be an iterable. To do this, you will need to define an __iter__ method within the class;
this method should be a generator, that returns one Loan at a time. Effectively, the result will be that you should be
able to loop over a LoanPool object's individual Loan objects

"""
from MortgageMixin import FixedRateMortgage
from assets.HouseBase import PrimaryHome as Primary
from assets.HouseBase import VacationHome as Vacation
from loan import FixedAutoLoan
from assets.Car import Civic
from assets.Car import Lexus
from loan import LoanPool


def main():
    print ('========== Exercise 3.2.3 ==========\n')

    myHome = FixedRateMortgage(Primary(200000), 360, .045, 200000)
    myVacation = FixedRateMortgage(Vacation(300000), 180, .055, 300000)
    myCivic = FixedAutoLoan(Civic(20000), 48, .075, 20000)
    myLexus = FixedAutoLoan(Lexus(35000), 72, .075, 40000)

    loanpool = LoanPool([myHome, myVacation, myCivic, myLexus])

    for i in loanpool:
        print (i)





if __name__ == '__main__':
    main()