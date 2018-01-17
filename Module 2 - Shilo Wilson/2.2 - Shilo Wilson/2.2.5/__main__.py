"""
Jan 14, 2018
Author: Shilo Wilson

Main function to test the loan class.

"""

from FixedAutoLoan import FixedAutoLoan as Auto
from LoanPool import LoanPool as LoanPool
def main():
    print ('========== Exercise 2.2.5 ==========\n')
    myloanpool = LoanPool(
        [
            Auto(60, .055, 12000),
            Auto(72, .065, 20000),
            Auto(48, .045, 8000)
        ]
    )

    print 'Total Principal {}'.format(myloanpool.totalPrincipal())
    print 'Total Balance in period 65: {}'.format(myloanpool.totalBalance(65))
    print myloanpool.aggregateInfo(65)
    print 'Active loans period 65: {}'.format(myloanpool.active(65))
    print 'WAR: {}'.format(myloanpool.WAR())
    print 'WAM: {}'.format(myloanpool.WAM())

if __name__ == '__main__':
    main()