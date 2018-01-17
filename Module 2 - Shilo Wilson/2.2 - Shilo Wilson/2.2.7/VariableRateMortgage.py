"""
Author: Shilo Wilson
VariableRateMortgage class to test Mixin
"""
from VariableRateLoan import VariableRateLoan as VariableLoan
from MortgageMixin import MortgageMixin as MortgageMixin
from assets.House.HouseBase import HouseBase as HouseBase

class VariableRateMortgage(MortgageMixin, VariableLoan):

    def __init__(self,asset, term, rate, face):
        super(VariableRateMortgage, self).__init__(asset, term, rate, face)

