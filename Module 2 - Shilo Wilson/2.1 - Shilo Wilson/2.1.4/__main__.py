"""
Jan 14, 2018
Author: Shilo Wilson

Main function to test the loan class.

"""

from loan import Loan as Loan
from Timer import Timer as timer


def main():


    print ('========== Exersize 2.1.4 ==========\n')

    print('Testing Loan classmethod for monthly payment : {}'.format(Loan.calcMonthlyPmt(100000, .025, 360)))
    print('Testing Loan classmethod for balance: {}'.format(Loan.calcBal(100000, .025, 360, 60)))

    myLoan = Loan(360,.025,100000)
    print("Monthly Payment: {}".format(myLoan.monthlyPayment()))
    print("Balance after 60 periods: {}".format(myLoan.balance(60)))
    print("Interest due on period 60: {}".format(myLoan.interestDue(60)))
    print("Principal due on period 60: {}".format(myLoan.principlaDue(60)))

    print("The total payment should equal interest plus principal which is {}".format(myLoan.interestDue(5) + myLoan.principlaDue(5)))
    print("Total Interest paid is {}".format(myLoan.totalInterest()))
    print("Total Payment is {}".format(myLoan.totalPayments()))
    print("Total Interest paid is {}".format(myLoan.totalInterest()))

    """
    The benefit of the cls level method is that it allows us to compute a payment or balance with out initiating an object
    """

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