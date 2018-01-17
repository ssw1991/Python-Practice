"""
Jan 14, 2018
Author: Shilo Wilson

Main function to test the loan class.

"""

from Mortgage import Mortgage as Mortgage

def main():
    print ('========== Exercise 2.2.2 ==========\n')

    myMortgage = Mortgage(360, .025, 100000)

    for i in range(37):
        print 'Period: {}, Balance: {}, Monthly payment: {}, Principal due: {}, Interest due: {}, PMI due: {}'.format(
            i*10, myMortgage.balance(i*10), myMortgage.monthlyPayment(i*10), myMortgage.principlaDue(i*10),
            myMortgage.interestDue(i*10),
            myMortgage.monthlyPayment(i*10) - myMortgage.principlaDue(i*10) - myMortgage.interestDue(i*10)
            )


if __name__ == '__main__':
    main()