"""
Author: Shilo Wilson
b.  A VariableRateLoan class which derives from Loan.  This should have its own __init__ function that sets a _rateDict
attribute on the object and then invokes the super-class
"""

from loan import Loan as Loan

class VariableRateLoan(Loan):

    def __init__(self, term, rateDict, face):
        self._rateDict = rateDict
        super(VariableRateLoan, self).__init__(term, None, face)

    @property
    def rateDict(self):
        return self._rateDict

    @rateDict.setter
    def rateDict(self, irateDict):
        self._rateDict = irateDict

    def rate(self, period):
        key = max([i for i in self._rateDict if i < period])
        return self._rateDict[key]


