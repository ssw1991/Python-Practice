"""
Jan 14, 2018
Author: Shilo Wilson

4) Modify all the applicable Loan classes from Level 2 so that if an incorrect Asset type is passed-into the __init__
function, an exception is raised (instead of printing the message to the user). Test this out in main, and handle the
exception.


I also made LoanPool raise an exception if there was a non loan passed in the list
"""
from MortgageMixin import FixedRateMortgage
from assets.HouseBase import PrimaryHome as Primary
from assets.HouseBase import VacationHome as Vacation
from loan import FixedAutoLoan
from assets.Car import Civic
from assets.Car import Lexus
from loan import LoanPool


def main():
    print ('========== Exercise 3.3.4 ==========\n')

    try:
        myHome = FixedRateMortgage(200000, 360, .045, 200000)
    except Exception as e:
        print e.message
        myHome = FixedRateMortgage(Primary(200000), 360, .045, 200000)
    try:
        myVacation = FixedRateMortgage(300000, 180, .055, 300000)
    except Exception as e:
        print e.message
        myVacation = FixedRateMortgage(Vacation(300000), 180, .055, 300000)
    try:
        myCivic = FixedAutoLoan(20000, 48, .075, 20000)
    except Exception as e:
        print e.message
        myCivic = FixedAutoLoan(Civic(20000), 48, .075, 20000)
    try:
        myLexus = FixedAutoLoan(35000, 72, .075, 40000)
    except Exception as e:
        print e.message
        myLexus = FixedAutoLoan(Lexus(35000), 72, .075, 40000)

    try:
        loanpool = LoanPool([myHome, myVacation, myCivic, myLexus, 0])
    except Exception as e:
        print e.message
        loanpool = LoanPool([myHome, myVacation, myCivic, myLexus])

    for i in loanpool:
        print (i)





if __name__ == '__main__':
    main()