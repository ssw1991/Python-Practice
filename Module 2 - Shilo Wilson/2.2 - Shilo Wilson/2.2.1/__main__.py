"""
Jan 14, 2018
Author: Shilo Wilson

Main function to test the loan class.

"""

from FixedRateLoan import FixedRateLoan as Fixed
from VariableRateLoan import VariableRateLoan as Variable


def main():
    print ('========== Exersize 2.2.1 ==========\n')

    myFixedLoan = Fixed(360,.025,100000)
    print("Monthly Payment: {}".format(myFixedLoan.monthlyPayment()))
    print("Balance after 60 periods: {}".format(myFixedLoan.balance(60)))
    print("Interest due on period 60: {}".format(myFixedLoan.interestDue(60)))
    print("Principal due on period 60: {}".format(myFixedLoan.principlaDue(60)))

    print("The total payment should equal interest plus principal which is {}".format(myFixedLoan.interestDue(5) + myFixedLoan.principlaDue(5)))
    print("Total Interest paid is {}".format(myFixedLoan.totalInterest()))
    print("Total Payment is {}".format(myFixedLoan.totalPayments()))
    print("Total Interest paid is {}".format(myFixedLoan.totalInterest()))



    print("Old rate {}".format(myFixedLoan.rate))
    print("Old term {}".format(myFixedLoan.term))
    print("Old face {}".format(myFixedLoan.face))

    myFixedLoan.rate = .035
    myFixedLoan.term = 60
    myFixedLoan.face = 20000

    print("New rate {}".format(myFixedLoan.rate))
    print("New term {}".format(myFixedLoan.term))
    print("New face {}".format(myFixedLoan.face))

    myVariableLoan = Variable(360, {0: .025, 120: .045}, 100000)
    print 'Variable loan rate at period 15: {}'.format(myVariableLoan.rate(15))
    print 'Variable loan rate at period 121: {}'.format(myVariableLoan.rate(121))

    myVariableLoan.rateDict = {0: .025, 120: .035, 240: .045}
    print 'Variable loan rate at period 15: {}'.format(myVariableLoan.rate(15))
    print 'Variable loan rate at period 121: {}'.format(myVariableLoan.rate(121))
    print 'Variable loan rate at period 241: {}'.format(myVariableLoan.rate(241))

if __name__ == '__main__':
    main()