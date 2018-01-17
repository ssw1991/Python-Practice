"""
Author: Shilo Wilson
FixedRateMortgage class to test Mixin
"""
from FixedRateLoan import FixedRateLoan as FixedLoan
from MortgageMixin import MortgageMixin as MortgageMixin

class FixedRateMortgage(MortgageMixin, FixedLoan):

    def __init__(self,term, rate, face):
        super(FixedRateMortgage, self).__init__(term, rate, face)
