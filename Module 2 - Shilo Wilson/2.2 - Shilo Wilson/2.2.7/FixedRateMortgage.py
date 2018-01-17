"""
Author: Shilo Wilson
FixedRateMortgage class to test Mixin
"""
from FixedRateLoan import FixedRateLoan as FixedLoan
from MortgageMixin import MortgageMixin as MortgageMixin
from assets.House.HouseBase import HouseBase


class FixedRateMortgage(MortgageMixin, FixedLoan):

    def __init__(self,asset, term, rate, face):
        super(FixedRateMortgage, self).__init__(asset, term, rate, face)


