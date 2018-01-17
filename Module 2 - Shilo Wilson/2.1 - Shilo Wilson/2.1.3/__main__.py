"""
Jan 14, 2018
Author: Shilo Wilson
Main function to test the loan class.

"""

from loan import Loan as Loan
from Timer import Timer as timer


def main():
    print ('========== Exersize 2.1.3 ==========\n')
    myLoan = Loan(360,.025,100000)
    print("Monthly Payment: {}".format(myLoan.monthlyPayment()))
    t = timer()
    t.start()
    print("Balance after 60 periods: {}".format(myLoan.balance(60)))
    t.end()
    t.start()
    print('Balance in period 60 computed recursivly {}'.format(myLoan.balanceRecursive(60, myLoan.face)))
    t.end()
    t.start()
    print("Interest due on period 60: {}".format(myLoan.interestDue(60)))
    t.end()
    t.start()
    print('Interest in period 60 computed recursivly {}'.format(myLoan.interestDueRecursive(60, myLoan.face)))
    t.end()
    t.start()
    print("Principal due on period 60: {}".format(myLoan.principlaDue(60)))
    t.end()
    t.start()
    print('Principal in period 60 computed recursivly {}'.format(myLoan.principalDueRecursive(60, myLoan.face)))
    t.end()

    """
    On my system, in both instances the direct and recursive versions of the function run to fast to comeup with a time besides 0
    However, I know that the recursive function is likely much slower
    """

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