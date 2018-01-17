"""
Jan 14, 2018
Author: Shilo Wilson

Main function to test the loan class.

"""

from loan import Loan as Loan
from Timer import Timer as timer


def main():
    print ('========== Exersize 2.1.5 ==========\n')
    print('Testing static method for monthly rate : {}'.format(Loan.monthlyRate(.025)))
    print('Testing testing static method for annual rate: {}'.format(Loan.annualRate(.01)))

    """
        The benefit of the static method is that neither the class nor the instance is passed in.  This allows us 
        to include functions that may be useful for the class, but do not directly rely on information in the class.
        From an organizational standpoint this makes it easier to organize the code.  For example, the rate conversion is
        not logically part of a loan object, however the loan class is where it makes most sense to include it.
    """

    myLoan = Loan(360,.025,100000)
    print("Monthly Payment: {}".format(myLoan.monthlyPayment()))
    print("Balance after 60 periods: {}".format(myLoan.balance(60)))
    print("Interest due on period 60: {}".format(myLoan.interestDue(60)))
    print("Principal due on period 60: {}".format(myLoan.principlaDue(60)))

    print("The total payment should equal interest plus principal which is {}".format(myLoan.interestDue(5) + myLoan.principlaDue(5)))
    print("Total Interest paid is {}".format(myLoan.totalInterest()))
    print("Total Payment is {}".format(myLoan.totalPayments()))
    print("Total Interest paid is {}".format(myLoan.totalInterest()))



    print("Old rate {}".format(myLoan.rate))
    print("Old term {}".format(myLoan.term))
    print("Old face {}".format(myLoan.face))

    myLoan.rate = .035
    myLoan.term = 60
    myLoan.face = 20000

    print("New rate {}".format(myLoan.rate))
    print("New term {}".format(myLoan.term))
    print("New face {}".format(myLoan.face))


if __name__ == '__main__':
    main()