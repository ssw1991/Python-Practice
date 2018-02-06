"""
Author: Shilo Wilson

Restructuring Files per Level 3 feedback

"""
from loan import FixedRateLoan as FixedLoan
from loan import VariableRateLoan as VariableLoan
from MortgageMixin import MortgageMixin as MortgageMixin
import logging
logging.basicConfig()
logger = logging.getLogger('__main__.{}'.format(__name__))


class FixedRateMortgage(MortgageMixin, FixedLoan):

    def __init__(self,asset, start, end, rate, face):
        super(FixedRateMortgage, self).__init__(asset, start, end, rate, face)

    def __str__(self):
        return('Fixed Rate Mortgages for {} months, with payment of {}').format(self.term, self.monthlyPayment(0))

    def to_dict(self):
        return {'Type': 'Fixed Rate Mortgage', 'Asset': str(self.asset),
                'Asset Value': self.asset.initialvalue,  'Face': self.face, 'Rate': self.rate,'Term': self.term}

class VariableRateMortgage(MortgageMixin, VariableLoan):

    def __init__(self,asset, start, end, rate, face):
        super(VariableRateMortgage, self).__init__(asset, start, end, rate, face)

    def __str__(self):
        return ('Variable Rate Mortgages for {} months, with payment of {}').format(self.term, self.monthlyPayment(0))

    def to_dict(self):
        return {'Type': 'Variable Rate Mortgage', 'Asset': str(self.asset),
                'Asset Value': self.asset.initialvalue,  'Face': self.face, 'Rate': self.rate,'Term': self.term}
