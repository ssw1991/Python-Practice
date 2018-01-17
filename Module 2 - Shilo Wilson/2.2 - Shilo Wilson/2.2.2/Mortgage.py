"""
Author: Shilo Wilson
Simple Mortgage class to test Mixin
"""
from loan import Loan as Loan
from MortgageMixin import MortgageMixin as MortgageMixin

class Mortgage(MortgageMixin, Loan):

    def __init__(self,term, rate, face):
        super(Mortgage, self).__init__(term, rate, face)
