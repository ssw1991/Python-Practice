"""
Jan 14, 2018
Author: Shilo Wilson

Main function to test the loan class.

"""

from FixedAutoLoan import FixedAutoLoan as Auto
def main():
    print ('========== Exercise 2.2.4 ==========\n')
    myAutoLoan = Auto(60, .065, 20000)

    print(myAutoLoan)
    print 'Amount due at period 15: Interest {}, Principal {}'.format(myAutoLoan.interestDue(15), myAutoLoan.principlaDue(15))


if __name__ == '__main__':
    main()