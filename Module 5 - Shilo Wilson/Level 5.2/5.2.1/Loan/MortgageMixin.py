"""
Author: Shilo Wilson

2)	Create a MortgageMixin class which will contain mortgage-specific methods. In particular, we'd like to implement the
concept of Private Mortgage Insurance (PMI). For those unaware, PMI is an extra monthly payment that one must make to
compensate for the added risk of having a Loan-to-Value (LTV) ratio of less than 80% (in other words, the loan covers >=
80% of the value of the asset).

To this end, implement a function called PMI that returns 0.0075% of the loan face value, but only if the LTV is < 80%.
For now, assume that the initial loan amount is for 100% of the asset value. Additionally, override the base class
monthlyPayment and principalDue functions to account for PMI (Hint: use super to avoid duplicating the formulas, and note
that the other methods (interestDue, balance, etc.) should not require any changes).

"""
from loan import FixedRateLoan as FixedLoan
from loan import VariableRateLoan as VariableLoan
from assets.HouseBase import HouseBase
import logging

logging.basicConfig()
logger = logging.getLogger('__main__.{}'.format(__name__))


class MortgageMixin(object):

    def __init__(self, asset, start, end, rate, face):
        """
        Calling super even though this does not derive from anything, because it will only be used when
        mixed into other classes (specifically, mortgaage will derive from this and loan
        """

        if isinstance(asset, HouseBase):
            super(MortgageMixin, self).__init__(asset, start, end, rate, face)
        else:
            logger.error('Wrong type for Asset.HouseBase')
            raise TypeError('Need a House for a Mortgage')


    def monthlyPayment(self, period):
        logger.debug('LTV is {}'.format(super(MortgageMixin, self).balance(period)))
        if super(MortgageMixin, self).balance(period) >= .8*self.face:
            return super(MortgageMixin, self).monthlyPayment() + .0075 * self.asset.initialvalue
        else:
            return super(MortgageMixin, self).monthlyPayment()

    def principalDue(self, period):
        logger.debug('LTV is {}'.format(super(MortgageMixin, self).balance(period)))
        if super(MortgageMixin, self).balance(period) >= .8 * self.face:
            return self.monthlyPayment(period) - self.interestDue(period) - .0075 * self.asset.initialvalue
        else:
            return super(MortgageMixin, self).principalDue(period)


