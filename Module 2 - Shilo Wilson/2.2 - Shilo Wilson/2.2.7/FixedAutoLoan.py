"""
Author: Shilo Wilson
4)	Create a fixed AutoLoan class. This should derive-from the appropriate base class(es).
"""
from FixedRateLoan import FixedRateLoan as loan
from assets.Car.Car import Car as Car

class FixedAutoLoan(loan):

    def __init__(self, asset, term, rate, face):
        if isinstance(asset, Car):
            super(FixedAutoLoan, self).__init__(asset,term, rate, face)
        else:
            print('Need a car for an AutoLoan')


    def __str__(self):
        """
        To make testing function calls eaiser
        """
        return 'Auto Loan for {} at {} for {} months, with payment of {}'.format(self.face, self.rate, self.term, self.monthlyPayment())
