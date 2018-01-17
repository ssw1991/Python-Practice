"""
Author: Shilo Wilson
VariableRateMortgage class to test Mixin
"""
from VariableRateLoan import VariableRateLoan as VariableLoan
from MortgageMixin import MortgageMixin as MortgageMixin

class VariableRateMortgage(MortgageMixin, VariableLoan):

    def __init__(self,term, rate, face, rateDict):
        super(VariableRateMortgage, self).__init__(term, rate, face, rateDict)
