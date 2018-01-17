"""
Author: Shilo Wilson
1)	As shown in the lecture, create derived classes as follows:
a.	A FixedRateLoan class which derives from Loan.

"""
from loan import Loan as Loan
class FixedRateLoan(Loan):

    def __init__(self, asset, term, rate, face):
        super(FixedRateLoan, self).__init__(asset, term, rate, face)

    def rate(self,period = 0):
        return self._rate