"""
Author: Shilo Wilson

Use memoization on the loan recursive function

I moved the utilities files inside the loan so that memoize could be
imported
"""

import logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel('WARN')

from Loan.mortgage import FixedRateMortgage as mortgage
from Loan.assets.HouseBase import PrimaryHome as Home
import datetime
from Loan.Utilities.Timer.Timer import Timer as Timer

@Timer
def getbal(ln, period, init_bal):
    """
    Using decorator outside of class because when I decorated inside the class
    the class was not passing the self parameter on
    :param ln:
    :param period:
    :param init_bal:
    :return:
    """
    ln.balanceRecursive(period, init_bal)
def main():
    print '========== Exercise 5.2.3 =========='
    start = datetime.date(2017, 01, 15)
    end =  datetime.date(2047, 01, 15)
    myLoan = mortgage(Home(500000), start, end, .025, 500000)

    getbal(myLoan, 320, 500000)
    getbal(myLoan, 320, 500000)

if __name__ == '__main__':
    main()