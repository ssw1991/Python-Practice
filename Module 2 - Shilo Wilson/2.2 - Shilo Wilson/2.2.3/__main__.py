"""
Jan 14, 2018
Author: Shilo Wilson

Main function to test the loan class.

"""

from FixedRateMortgage import FixedRateMortgage as FixedMortgage
from VariableRateMortgage import VariableRateMortgage as VariableMortgage
def main():
    print ('========== Exercise 2.2.3 ==========\n')

    myFixedMortgage = FixedMortgage(360, .025, 100000)


    for i in range(4):
        print 'Period: {}, Balance: {}, Monthly payment: {}, Principal due: {}, Interest due: {}, PMI due: {}'.format(
            i*120, myFixedMortgage.balance(i*120), myFixedMortgage.monthlyPayment(i*120), myFixedMortgage.principlaDue(i*120),
            myFixedMortgage.interestDue(i*120),
            myFixedMortgage.monthlyPayment(i*120) - myFixedMortgage.principlaDue(i*120) - myFixedMortgage.interestDue(i*120)
         )
    myVariableMortgage = VariableMortgage(360, {0: .025, 120: .045, 240: .055}, 100000)

    for i in range(4):
        print 'Period: {}, Balance: {}, Monthly payment: {}, Principal due: {}, Interest due: {}, PMI due: {}, Rate: {}'.format(
            i * 120, myVariableMortgage.balance(i * 120), myVariableMortgage.monthlyPayment(i * 120),
            myVariableMortgage.principlaDue(i * 120),
            myVariableMortgage.interestDue(i * 120),
            myVariableMortgage.monthlyPayment(i * 120) - myVariableMortgage.principlaDue(
                i * 120) - myVariableMortgage.interestDue(i * 120), myVariableMortgage.rate(i*120)
        )


if __name__ == '__main__':
    main()