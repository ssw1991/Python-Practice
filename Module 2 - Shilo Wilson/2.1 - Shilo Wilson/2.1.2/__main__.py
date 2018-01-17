"""
Author: Shilo Wilson
Main Function to test Loan

"""
from loan import Loan as Loan

def main():

    print('========== Exercise 2.1.2 ==========')
    myLoan = Loan(360,.025,100000)
    print("Monthly Payment: {}".format(myLoan.monthlyPayment()))
    print("Balance after 360 periods: {}".format(myLoan.balance(360)))
    print("Interest due on period 360: {}".format(myLoan.interestDue(360)))
    print("Principal due on period 360: {}".format(myLoan.principlaDue(360)))
    print("The total payment should equal interest plus principal which is {}".format(myLoan.interestDue(5) + myLoan.principlaDue(5)))
    print("Total Interest paid is {}".format(myLoan.totalInterest()))
    print("Total Payment is {}".format(myLoan.totalPayments()))


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