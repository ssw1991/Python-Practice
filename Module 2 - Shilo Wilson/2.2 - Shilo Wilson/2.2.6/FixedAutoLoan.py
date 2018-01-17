"""
Author: Shilo Wilson
4)	Create a fixed AutoLoan class. This should derive-from the appropriate base class(es).
"""
from FixedRateLoan import FixedRateLoan as loan
class FixedAutoLoan(loan):

    def __init__(self, term, rate, face):
        super(FixedAutoLoan, self).__init__(term, rate, face)

    def __str__(self):
        """
        To make testing function calls eaiser
        """
        return 'Auto Loan for {} at {} for {} months, with payment of {}'.format(self.face, self.rate, self.term, self.monthlyPayment())
